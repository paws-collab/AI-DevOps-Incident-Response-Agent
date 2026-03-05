# agent/incident_agent.py

from transformers import pipeline

from tools.severity_tool import classify_severity
from tools.fix_suggester import suggest_fix
from tools.report_generator import generate_report
from agent.reflection import reflect_analysis


llm_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)


def call_llm(prompt: str) -> str:
    result = llm_pipeline(prompt)
    return result[0]["generated_text"]


def run_agent(context: str) -> dict:

    # Step 1: Root Cause Analysis
    analysis_prompt = f"""
    You are an expert production support engineer.

    Analyze the following logs and identify:
    - Root cause
    - Possible issue
    - Impact

    Logs:
    {context}
    """

    analysis = call_llm(analysis_prompt)

    # Step 2: AI Severity
    severity = classify_severity(context)

    # Step 3: AI Fix Suggestion
    fix = suggest_fix(context)

    # Step 4: Reflection layer
    reflection = reflect_analysis(
        context,
        analysis,
        severity,
        fix
    )

    # Step 5: Report
    report = generate_report(
        context=context,
        analysis=analysis,
        severity=severity,
        fix=fix
    )

    return {
        "analysis": analysis,
        "severity": severity,
        "fix": fix,
        "reflection": reflection,
        "report": report
    }