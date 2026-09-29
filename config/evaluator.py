from deepeval.models import OllamaModel


# =========================================================
# DEEPEVAL EVALUATOR MODEL
# =========================================================

evaluator_model = OllamaModel(
    model="qwen3:4b-instruct",
    temperature=0,
)