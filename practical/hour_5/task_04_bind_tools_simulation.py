"""
PRACTICAL CHALLENGE: Simulating model.bind_tools() (LC-H5-P04)
=====================================================
ID: LC-H5-P04
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement a `BindToolsModel` class that accepts a list of registered tools and simulates
deciding between a direct text answer and generating tool calls based on user input keywords.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_02_ai_message_with_tools import AIMessage

class BindToolsModel:
    def __init__(self, tools: list):
        self.tools_by_name = {getattr(t, "name", t.__name__): t for t in tools}

    def invoke(self, messages: list) -> AIMessage:
        last_text = messages[-1].content.lower()
        if "add" in last_text:
            return AIMessage(tool_calls=[{"name": "add", "args": {"a": 20, "b": 30}, "id": "call_1"}])
        elif "multiply" in last_text:
            return AIMessage(tool_calls=[{"name": "multiply", "args": {"a": 4, "b": 5}, "id": "call_2"}])
        return AIMessage(content="I can answer general questions directly.")

def add(a: int, b: int) -> int: return a + b
def multiply(a: int, b: int) -> int: return a * b

class MockMsg:
    def __init__(self, c): self.content = c

def test_bind_tools_model():
    model = BindToolsModel([add, multiply])
    ai_res = model.invoke([MockMsg("Please add 20 and 30")])
    assert ai_res.has_tool_calls
    assert ai_res.tool_calls[0]["name"] == "add"

    ai_text = model.invoke([MockMsg("What is your purpose?")])
    assert not ai_text.has_tool_calls
    assert "general questions" in ai_text.content

if __name__ == '__main__':
    test_bind_tools_model()
    print("✓ Task 04 passed!")
