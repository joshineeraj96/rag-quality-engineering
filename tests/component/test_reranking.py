import pytest
import json

from utils.rag_reranking import get_reranked_documents


with open("datasets/golden_dataset/rag_golden_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


@pytest.mark.regression
@pytest.mark.parametrize("test_case_data", test_data, ids=[test_case["question"] for test_case in test_data])
def test_reranking(test_case_data):

    question = test_case_data["question"]

    documents = get_reranked_documents(
        question
    )

    assert len(documents) > 0

    scores = [
        document["score"]
        for document in documents
    ]

    assert all(
        1 <= score <= 5
        for score in scores
    )

    assert scores == sorted(
        scores,
        reverse=True
    )