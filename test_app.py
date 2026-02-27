from agent.incident_agent import run_agent
#I added automated testing using pytest to ensure reliability and code quality.
def test_incident_analysis():
    log = """
    ERROR Application crashed with OutOfMemoryException.
    System.OutOfMemoryException: Exception of type 'System.OutOfMemoryException' was thrown.
    """

    result = run_agent(log)

    # ✅ Correct assertions
    assert result["severity"] == "Critical"
    assert "OutOfMemoryException" in result["analysis"]
    assert "memory" in result["fix"].lower()