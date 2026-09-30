"""
PRACTICAL CHALLENGE: Tool Parameter Schema Inspection (LC-H4-P09)
=====================================================
ID: LC-H4-P09
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a schema generator `extract_tool_schema(tool)` that produces a JSON-compatible
schema containing parameter names, types, and default values from type hints.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import inspect

def extract_tool_schema(func) -> dict:
    sig = inspect.signature(func)
    params = {}
    for name, p in sig.parameters.items():
        type_name = p.annotation.__name__ if p.annotation != inspect.Parameter.empty else "any"
        has_default = p.default != inspect.Parameter.empty
        params[name] = {
            "type": type_name,
            "required": not has_default,
            "default": p.default if has_default else None
        }
    return {
        "name": func.__name__,
        "description": (func.__doc__ or "").strip(),
        "parameters": params
    }

def multiply(x: int, y: int = 1) -> int:
    """Multiply two integers."""
    return x * y

def test_schema_extraction():
    schema = extract_tool_schema(multiply)
    assert schema["name"] == "multiply"
    assert schema["description"] == "Multiply two integers."
    assert schema["parameters"]["x"]["type"] == "int"
    assert schema["parameters"]["x"]["required"] is True
    assert schema["parameters"]["y"]["default"] == 1

if __name__ == '__main__':
    test_schema_extraction()
    print("✓ Task 09 passed!")
