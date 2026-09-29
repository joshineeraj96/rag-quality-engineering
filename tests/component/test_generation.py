import pytest
import json

from utils.rag_generation import generate_answer
from utils.rag_retrieval import get_documents
from deepeval.test_case import LLMTestCase
from config.metrics import generation_metrics
from deepeval import assert_test



# =========================================================
# LOAD GOLDEN DATASET
# =========================================================

with open("datasets/golden_dataset/rag_golden_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


@pytest.mark.regression
@pytest.mark.parametrize("test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_generation(test_case_data):

    question = test_case_data["question"]

    # Get retrieval context
    documents = get_documents(
        question,
        "hybrid"
    )

    assert len(documents) > 0

    contexts = [
        doc["content"]
        for doc in documents
    ]

    # Generate answer
    context = "\n\n".join(contexts)

    answer = generate_answer(
        question,
        context
    )

    assert answer

    test_case = LLMTestCase(
        input=question,
        actual_output=answer,
        retrieval_context=contexts
    )

    assert_test(test_case, generation_metrics)
