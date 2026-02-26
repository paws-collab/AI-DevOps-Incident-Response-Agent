# tools/report_generator.py

def generate_report(context, analysis, severity, fix):
    report = f"""
================ INCIDENT REPORT ================

📌 Logs:
{context}

🔍 Root Cause Analysis:
{analysis}

🚨 Severity:
{severity}

🛠 Suggested Fix:
{fix}

=================================================
"""
    return report