# tools/severity_tool.py

from transformers import pipeline

# Load model once
severity_llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=50
)

def classify_severity(log_text: str) -> str:
    prompt = f"""
    You are a DevOps incident management expert.

    Analyze the log and classify severity.

    Severity levels:
    Low
    Medium
    High
    Critical

    Log:
    {log_text}

    Answer with only the severity level.
    """

    result = severity_llm(prompt)
    return result[0]["generated_text"].strip()