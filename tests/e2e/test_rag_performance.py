import json
import pytest
import time
from statistics import quantiles


# =========================================================
# LOAD GOLDEN DATASET
# =========================================================
with open("datasets/golden_dataset/rag_golden_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


@pytest.mark.performance
def test_rag_performance(api_request, test_case_data):

    latencies = []

    for test_case_date in test_data:
        question = test_case_data["question"]

        start_time = time.perf_counter()

        response = api_request.post(
            "http://localhost:8000/query",
            data= {"data": question},
            timeout=180000,
        )

        end_time = time.perf_counter()

        latency = end_time - start_time

        latencies.append(latency)

        assert response.status == 200

    latencies.sort()


    p50 = quantiles(latencies, n=100)[49]
    p95 = quantiles(latencies, n=100)[94]
    p99 = quantiles(latencies, n=100)[98]


    print(f"\nP50: {p50:.2f}s")
    print(f"P95: {p95:.2f}s")
    print(f"P99: {p99:.2f}s")

    LATENCY_THRESHOLD = 60  # seconds

    assert p95 <= LATENCY_THRESHOLD, (
    f"P95 latency {p95:.2f}s exceeded "
    f"threshold of {LATENCY_THRESHOLD}s"
    )