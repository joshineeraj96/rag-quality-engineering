from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
)

from config.evaluator import evaluator_model


metrics = [
    AnswerRelevancyMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    FaithfulnessMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    ContextualRelevancyMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    ContextualPrecisionMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    ContextualRecallMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
]


retrieval_metrics = [
    ContextualRelevancyMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    ContextualPrecisionMetric(
        threshold=0.7,
        model=evaluator_model,
    ),
    ContextualRecallMetric(
        threshold=0.7,
        model=evaluator_model,
    )
]

generation_metrics = [
    AnswerRelevancyMetric(
        threshold=0.7,
        model=evaluator_model
    ),
    FaithfulnessMetric(
        threshold=0.7,
        model=evaluator_model
    )
]   