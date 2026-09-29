import pytest
import json

from utils.rag_retrieval import get_documents
from deepeval.test_case import LLMTestCase
from config.metrics import retrieval_metrics
from deepeval import assert_test



# =========================================================
# LOAD GOLDEN DATASET
# =========================================================

with open("datasets/golden_dataset/rag_golden_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


@pytest.mark.regression
@pytest.mark.parametrize("test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_semantic_retrieval(test_case_data):

    question = test_case_data["question"]
    expected_answer = test_case_data["expected_answer"]

    documents = get_documents(question, "semantic")

    assert len(documents) > 0

    contexts = [doc["content"] for doc in documents]

    test_case = LLMTestCase(
        input=question,
        expected_output=expected_answer,
        retrieval_context=contexts
    )

    assert_test(test_case, retrieval_metrics)


@pytest.mark.regression
@pytest.mark.parametrize("test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_bm25_retrieval(test_case_data):

    question = test_case_data["question"]
    expected_answer = test_case_data["expected_answer"]

    documents = get_documents(question, "bm25")

    assert len(documents) > 0

    contexts = [doc["content"] for doc in documents]

    test_case = LLMTestCase(
        input=question,
        expected_output=expected_answer,
        retrieval_context=contexts
    )

    assert_test(test_case, retrieval_metrics)


@pytest.mark.regression
@pytest.mark.parametrize(
    "test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_hybrid_retrieval(test_case_data):

    question = test_case_data["question"]
    expected_answer = test_case_data["expected_answer"]

    documents = get_documents(question, "hybrid")

    assert len(documents) > 0

    contexts = [doc["content"] for doc in documents]

    test_case = LLMTestCase(
        input=question,
        expected_output=expected_answer,
        retrieval_context=contexts
    )

    assert_test(test_case, retrieval_metrics)