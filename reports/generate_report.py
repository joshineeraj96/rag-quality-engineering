import json
from pathlib import Path

json_file = Path("reports/deepeval/.latest_run_full.json")

with open(json_file, encoding="utf-8") as file:
    report = json.load(file)

html = "<h1>RAG Quality Report</h1>"

html += """
<table border="1">
<tr>
    <th>Metric</th>
    <th>Score</th>
    <th>Threshold</th>
    <th>Status</th>
    <th>Reason</th>
</tr>
"""

for test_case in report["testCases"]:
    for metric in test_case["metricsData"]:
        html += f"""
<tr>
    <td>{metric["name"]}</td>
    <td>{metric["score"]}</td>
    <td>{metric["threshold"]}</td>
    <td>{"PASS" if metric["success"] else "FAIL"}</td>
    <td>{metric["reason"]}</td>
</tr>
"""

html += "</table>"

Path("reports/rag_quality_report.html").write_text(
    html,
    encoding="utf-8"
)

print("Report created: reports/rag_quality_report.html")