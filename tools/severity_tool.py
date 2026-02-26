def classify_severity(log_text: str) -> str:
    log_text = log_text.lower()

    if "outofmemory" in log_text:
        return "Critical"
    elif "timeout" in log_text:
        return "High"
    elif "error" in log_text:
        return "Medium"
    else:
        return "Low"