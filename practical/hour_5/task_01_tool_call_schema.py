"""
PRACTICAL CHALLENGE: Tool Call Representation & Validation (LC-H5-P01)
=====================================================
ID: LC-H5-P01
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement a `ToolCall` dataclass or dictionary representation with fields `name` (str),
`args` (dict), and `id` (str). Validate that `id` is a non-empty string and `args` is a valid dict.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from dataclasses import dataclass, field

@dataclass
class ToolCall:
    name: str
    args: dict
    id: str

    def __post_init__(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("ToolCall name must be a non-empty string.")
        if not isinstance(self.args, dict):
            raise TypeError("ToolCall args must be a dictionary.")
        if not self.id or not isinstance(self.id, str):
            raise ValueError("ToolCall id must be a non-empty string.")

def test_tool_call():
    tc = ToolCall(name="add", args={"a": 5, "b": 10}, id="call_12345")
    assert tc.name == "add"
    assert tc.args["a"] == 5
    assert tc.id == "call_12345"

    try:
        ToolCall(name="add", args="invalid_args", id="call_1")
        assert False, "Should raise TypeError"
    except TypeError:
        pass

if __name__ == '__main__':
    test_tool_call()
    print("✓ Task 01 passed!")
