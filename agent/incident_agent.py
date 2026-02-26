# agent/incident_agent.py

# ✅ IMPORT CONFIG (optional if you still use it elsewhere)
import config  

# ✅ Local FREE LLM (no OpenAI required)
from transformers import pipeline

# ✅ Your custom tools
from tools.severity_tool import classify_severity
from tools.fix_suggester import suggest_fix
from tools.report_generator import generate_report


# ✅ Load FREE HuggingFace model (runs locally)
llm_pipeline = pipeline(
    "text2text-generation",   # ✅ FIXED
    model="google/flan-t5-base",
    max_length=512
)


# ✅ Wrapper function for LLM call
def call_llm(prompt: str) -> str:
    try:
        result = llm_pipeline(prompt)
        return result[0]["generated_text"]
    except Exception as e:
        return f"LLM Error: {str(e)}"


# ✅ MAIN AGENT FUNCTION
def run_agent(context: str) -> dict:
    """
    Runs AI Incident Analysis Agent

    Args:
        context (str): Logs / error context from RAG

    Returns:
        dict: structured result with analysis, severity, fix, report
    """

    # 🔍 Step 1: Root Cause Analysis
    analysis_prompt = f"""
    You are an expert production support engineer.

    Analyze the following logs and identify:
    - Root cause
    - Possible issue
    - Impact

    Logs:
    {context}

    Give clear explanation.
    """

    analysis = call_llm(analysis_prompt)

    # 🚨 Step 2: Severity Classification
    severity = classify_severity(context)

    # 🛠 Step 3: Suggested Fix
    fix = suggest_fix(context)

    # 📄 Step 4: Generate Final Report
    report = generate_report(
        context=context,
        analysis=analysis,
        severity=severity,
        fix=fix
    )

    # ✅ Final Output
    return {
        "analysis": analysis,
        "severity": severity,
        "fix": fix,
        "report": report
    }