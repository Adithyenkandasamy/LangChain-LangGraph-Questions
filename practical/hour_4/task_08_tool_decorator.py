"""
PRACTICAL CHALLENGE: Custom @tool Decorator (LC-H4-P08)
=====================================================
ID: LC-H4-P08
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a `@tool` decorator that wraps a Python function, extracts its name, docstring,
and parameter schema, and provides an `.invoke(kwargs)` method.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import inspect

class Tool:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.description = (func.__doc__ or "").strip()
        self.signature = inspect.signature(func)

    def invoke(self, kwargs: dict):
        return self.func(**kwargs)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

def tool(func):
    return Tool(func)

@tool
def add(a: int, b: int) -> int:
    """Add two integer numbers together."""
    return a + b

def test_tool_decorator():
    assert add.name == "add"
    assert add.description == "Add two integer numbers together."
    assert add.invoke({"a": 3, "b": 7}) == 10
    assert add(4, 5) == 9

if __name__ == '__main__':
    test_tool_decorator()
    print("✓ Task 08 passed!")
