"""
PRACTICAL CHALLENGE: Centralized Tool Registry (LC-H4-P12)
=====================================================
ID: LC-H4-P12
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a `ToolRegistry` that registers tools, prevents duplicate names,
lists registered tools, and allows lookup by tool name.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool_func):
        name = getattr(tool_func, "name", tool_func.__name__)
        if name in self._tools:
            raise ValueError(f"Tool '{name}' is already registered.")
        self._tools[name] = tool_func

    def get(self, name: str):
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not found.")
        return self._tools[name]

    def list_names(self) -> list:
        return sorted(list(self._tools.keys()))

def test_tool_registry():
    registry = ToolRegistry()
    def search_web(query: str) -> str: """Search web"""; return ""
    def calculator(expr: str) -> str: """Calc"""; return ""

    registry.register(search_web)
    registry.register(calculator)

    assert registry.list_names() == ["calculator", "search_web"]
    assert registry.get("calculator") == calculator

    try:
        registry.register(search_web)
        assert False, "Duplicate registration should raise ValueError"
    except ValueError:
        pass

if __name__ == '__main__':
    test_tool_registry()
    print("✓ Task 12 passed!")
