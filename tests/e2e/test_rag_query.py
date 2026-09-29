import pytest


@pytest.mark.regression
def test_rag_query_empty_question(api_request):

    response = api_request.post(
        "http://localhost:8000/query",
        data={"question": ""},
        timeout=180000,
    )

    assert response.status == 400

    response_data = response.json()

    assert response_data["detail"] == "Question cannot be empty"

@pytest.mark.regression
def test_rag_query_missing_question(api_request):
    response = api_request.post(
        "http://localhost:8000/query",
        data={},
        timeout=180000
    )

    assert response.status == 422

@pytest.mark.regression
def test_rag_query_invalid_question_type(api_request):
    response = api_request.post(
        "http://localhost:8000/query",
        data={"question": 1234},
        timeout=180000
    )

    assert response.status == 422

@pytest.mark.regression
def test_rag_query_response_schema(api_request):

    response = api_request.post(
        "http://localhost:8000/query",
        data={"question": "What is the SI unit of weight?"},
        timeout=180000,
    )

    assert response.status == 200

    response_data = response.json()

    assert "answer" in response_data
    assert "retrieval_context" in response_data
    assert isinstance(response_data["answer"], str)
    assert isinstance(response_data["retrieval_context"], list)


@pytest.mark.regression
def test_rag_query_unknown_question(api_request):

    response = api_request.post(
        "http://localhost:8000/query",
        data={"question": "Who is the President of the United States?"},
        timeout=180000,
    )

    assert response.status == 200

    response_data = response.json()

    assert "I don't have enough information." in response_data["answer"]


@pytest.mark.regression
def test_rag_query_follow_up(api_request):

    first_response = api_request.post(
        "http://localhost:8000/query",
        data={"question": "What is the weight of an object?"},
        timeout=180000,
    )

    assert first_response.status == 200

    session_cookie = first_response.headers.get("set-cookie")

    assert session_cookie is not None

    second_response = api_request.post(
        "http://localhost:8000/query",
        data={"question": "What is its SI unit?"},
        headers={"Cookie": session_cookie},
        timeout=180000,
    )

    assert second_response.status == 200

    second_response_data = second_response.json()

    assert "pascal" in second_response_data["answer"].lower()