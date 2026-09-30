"""
PRACTICAL CHALLENGE: Two-Turn LLM Tool Execution Loop (LC-H5-P06)
=====================================================
ID: LC-H5-P06
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Implement a two-turn loop `run_tool_turn(history, model, tools_map)`:
Turn 1: Model returns tool call
Turn 2: Tool executes and adds ToolMessage, Model runs again to produce final natural language answer.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from task_02_ai_message_with_tools import AIMessage
from task_03_tool_message import ToolMessage
from task_05_tool_dispatcher import dispatch_tool_calls

class MockTwoTurnModel:
    def invoke(self, history: list) -> AIMessage:
        # Check if last message is a ToolMessage
        if history and getattr(history[-1], "role", "") == "tool":
            return AIMessage(content=f"The answer is {history[-1].content}.")
        return AIMessage(tool_calls=[{"name": "calc", "args": {"x": 7, "y": 6}, "id": "call_calc_1"}])

def run_tool_turn(history: list, model, tools_map: dict) -> AIMessage:
    first_response = model.invoke(history)
    if not first_response.has_tool_calls:
        return first_response

    history.append(first_response)
    tool_msgs = dispatch_tool_calls(first_response.tool_calls, tools_map)
    history.extend(tool_msgs)

    final_response = model.invoke(history)
    history.append(final_response)
    return final_response

def test_two_turn_loop():
    tools = {"calc": lambda x, y: x * y}
    model = MockTwoTurnModel()
    history = []

    final_ans = run_tool_turn(history, model, tools)
    assert final_ans.content == "The answer is 42."
    assert len(history) == 3 # AIMessage(calls) + ToolMessage + AIMessage(final)

if __name__ == '__main__':
    test_two_turn_loop()
    print("✓ Task 06 passed!")
