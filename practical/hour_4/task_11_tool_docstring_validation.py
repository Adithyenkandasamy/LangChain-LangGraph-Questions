"""
PRACTICAL CHALLENGE: Enforcing Tool Docstring Standards (LC-H4-P11)
=====================================================
ID: LC-H4-P11
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a validator `validate_tool_definition(func)` that checks if a tool has a non-empty
docstring, valid type annotations on all parameters, and a return type annotation.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import inspect

def validate_tool_definition(func):
    doc = func.__doc__
    if not doc or not doc.strip():
        raise ValueError(f"Tool '{func.__name__}' must contain a descriptive docstring.")
    
    sig = inspect.signature(func)
    for name, p in sig.parameters.items():
        if p.annotation == inspect.Parameter.empty:
            raise TypeError(f"Parameter '{name}' in tool '{func.__name__}' lacks type annotation.")
            
    if sig.return_annotation == inspect.Parameter.empty:
        raise TypeError(f"Tool '{func.__name__}' must have a return type annotation.")
    return True

def valid_tool(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

def invalid_tool(a, b):
    return a + b

def test_tool_docstring_validation():
    assert validate_tool_definition(valid_tool) is True

    try:
        validate_tool_definition(invalid_tool)
        assert False, "Should fail on missing docstring/types"
    except (ValueError, TypeError):
        pass

if __name__ == '__main__':
    test_tool_docstring_validation()
    print("✓ Task 11 passed!")
