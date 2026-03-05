# tests/test_app.py

from agent.incident_agent import run_agent


# Test 1: OutOfMemory incident
def test_outofmemory_incident():

    log = """
    ERROR Application crashed with OutOfMemoryException.
    System.OutOfMemoryException: Exception of type 'System.OutOfMemoryException' was thrown.
    """

    result = run_agent(log)

    # Severity should be High or Critical
    assert result["severity"] in ["High", "Critical"]

    # Fix should mention memory
    assert "memory" in result["fix"].lower()

    # Analysis should exist
    assert isinstance(result["analysis"], str)


# Test 2: Database timeout incident
def test_timeout_incident():

    log = """
    ERROR Database request timeout after 30 seconds.
    SQL query execution exceeded allowed time.
    """

    result = run_agent(log)

    # Severity likely High or Medium
    assert result["severity"] in ["High", "Medium"]

    # Fix should mention timeout or query optimization
    assert "timeout" in result["fix"].lower() or "query" in result["fix"].lower()

    assert isinstance(result["analysis"], str)


# Test 3: Generic application error
def test_generic_error():

    log = """
    ERROR Unexpected application failure during request processing.
    """

    result = run_agent(log)

    # Severity should still be valid
    assert result["severity"] in ["Low", "Medium", "High", "Critical"]

    # Ensure AI generated analysis
    assert isinstance(result["analysis"], str)

    # Ensure fix exists
    assert isinstance(result["fix"], str)