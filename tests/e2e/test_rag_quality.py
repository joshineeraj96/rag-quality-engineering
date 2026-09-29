import json

import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase

from config.metrics import metrics


# =========================================================
# LOAD GOLDEN DATASET
# =========================================================

with open("datasets/golden_dataset/rag_golden_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


# =========================================================
# RAG QUALITY TEST
# =========================================================

@pytest.mark.regression
@pytest.mark.parametrize("test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_rag_quality(api_request, test_case_data):

    # Get test data
    question = test_case_data["question"]
    expected_answer = test_case_data["expected_answer"]

    # Call RAG API
    response = api_request.post(
        "http://localhost:8000/query",
        data={"question": question},
        timeout=180000,
    )

    assert response.status == 200

    response_data = response.json()

    # Create DeepEval test case
    test_case = LLMTestCase(
        input=question,
        actual_output=response_data["answer"],
        retrieval_context=response_data["retrieval_context"],
        expected_output=expected_answer,
    )

    # Run DeepEval metrics
    assert_test(test_case, metrics)