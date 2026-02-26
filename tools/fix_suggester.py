def suggest_fix(log_text: str) -> str:
    log_text = log_text.lower()

    if "outofmemory" in log_text:
        return "Increase memory allocation or investigate memory leaks."
    elif "timeout" in log_text:
        return "Optimize database queries or increase timeout configuration."
    elif "nullreferenceexception" in log_text:
        return "Add null checks and validate object initialization."
    else:
        return "Review stack trace and application logs for further investigation."