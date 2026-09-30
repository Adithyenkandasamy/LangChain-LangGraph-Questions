"""
PRACTICAL CHALLENGE: Safe Tool Execution & Error Recovery (LC-H4-P13)
=====================================================
ID: LC-H4-P13
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement `safe_execute_tool(tool_func, kwargs)` that executes a tool, catches exceptions,
and returns an informative error string instead of crashing the pipeline.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def safe_execute_tool(tool_func, kwargs: dict) -> str:
    try:
        result = tool_func(**kwargs)
        return str(result)
    except Exception as e:
        return f"Error executing {tool_func.__name__}: {type(e).__name__} - {str(e)}"

def divide(a: float, b: float) -> float:
    return a / b

def test_safe_tool_execution():
    res1 = safe_execute_tool(divide, {"a": 10.0, "b": 2.0})
    assert res1 == "5.0"

    res2 = safe_execute_tool(divide, {"a": 10.0, "b": 0.0})
    assert "ZeroDivisionError" in res2

if __name__ == '__main__':
    test_safe_tool_execution()
    print("✓ Task 13 passed!")
