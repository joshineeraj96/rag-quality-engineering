import json


# =========================================================
# LOAD SECURITY DATASET
# =========================================================
with open("datasets/security/security_dataset.json", encoding="utf-8") as file:
    test_data = json.load(file)


def get_security_cases(category):
    result = []

    for test_case in test_data:
        if test_case["category"] == category:
            result.append(test_case)

    return result