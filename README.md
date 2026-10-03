# RAG Quality Engineering Framework

A Python-based test automation framework for testing a Retrieval-Augmented Generation (RAG) application.

The framework focuses on validating the main RAG flow through API/E2E tests and component-level tests where the required component interfaces are available.

## What This Framework Tests

* RAG query API behavior
* Retrieval and retrieved context
* Reranking results
* Generated answers
* RAG quality metrics
* Response validation
* Security-related scenarios
* Regression test cases
* Performance and latency testing
* P50, P95 and P99 latency measurement
* P95 latency threshold validation

## Test Approach

The framework contains two main levels of testing:

### Component Tests

Validate individual RAG components where they can be accessed through legitimate testable interfaces.

Examples:

* Retrieval
* Reranking
* Generation
* Context-related validation

### E2E Tests

Validate the complete RAG flow through the application's public API.

Example flow:

```text
User Question
     ↓
RAG API
     ↓
Query Transformation
     ↓
Hybrid Retrieval
     ↓
Reranking
     ↓
Context
     ↓
LLM Generation
     ↓
Response
```

## Tools & Technologies

* Python
* Pytest
* Playwright API
* RAGAS
* DeepEval
* LangSmith
* FastAPI
* Chroma
* Ollama

## Project Structure

```text
rag-quality-engineering/

│
├── config/
│   └── security_metrics.py
│
├── datasets/
│   └── golden_dataset/
│
├── reports/
│   └── generate_report.py
│
├── tests/
│   ├── component/
│   └── e2e/
│       ├── test_rag_query.py
│       ├── test_rag_quality.py
│       ├── test_rag_security.py
│       └── test_rag_performance.py
│
├── utils/
│   └── security_data.py
│
├── conftest.py
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Running Tests

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run all tests:

```powershell
pytest -v
```

Run E2E tests:

```powershell
pytest tests/e2e -v
```

Run a specific test file:

```powershell
pytest tests/e2e/test_rag_query.py -v
```

Run performance tests:

```powershell
pytest tests/e2e/test_rag_performance.py -v
```

## Reporting

The framework can generate test reports and RAG evaluation results.

The project also uses LangSmith for tracing and debugging the RAG execution flow.

## Performance Testing

The framework includes basic RAG performance testing using the golden dataset.

Performance tests measure end-to-end API latency and calculate:

* P50 latency
* P95 latency
* P99 latency

A P95 latency threshold is used as a performance quality gate.

The same golden dataset is reused for performance testing to avoid maintaining duplicate test data.

Basic cost-testing concepts are also considered, including token usage and estimated cost per request. The current local Ollama setup does not provide a real API billing cost.

## Current Scope

The current implementation focuses on the core RAG testing flow, practical quality validation, security testing, and basic performance validation.

It does not attempt to cover every possible RAG evaluation technique or AI testing scenario.

Future areas can be added based on project requirements and testing needs.

## Note

This is a test automation framework built around a separate RAG application used as the system under test (SUT).

The framework is intended to demonstrate practical RAG quality engineering and test automation concepts rather than provide a complete RAG testing product.
