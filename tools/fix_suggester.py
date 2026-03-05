# tools/fix_suggester.py

from transformers import pipeline

fix_llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=120
)

def suggest_fix(log_text: str) -> str:

    prompt = f"""
    You are a senior DevOps engineer.

    Analyze the following production log
    and suggest a practical fix.

    Log:
    {log_text}

    Provide a short remediation step.
    """

    result = fix_llm(prompt)
    return result[0]["generated_text"].strip()