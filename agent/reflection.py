# agent/reflection.py

from transformers import pipeline

reflection_llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=150
)

def reflect_analysis(log, analysis, severity, fix):

    prompt = f"""
    A DevOps AI agent analyzed a production incident.

    Log:
    {log}

    Root Cause Analysis:
    {analysis}

    Predicted Severity:
    {severity}

    Suggested Fix:
    {fix}

    Verify if the fix actually resolves the root cause.

    If not, improve the fix.

    Return improved response.
    """

    result = reflection_llm(prompt)

    return result[0]["generated_text"]