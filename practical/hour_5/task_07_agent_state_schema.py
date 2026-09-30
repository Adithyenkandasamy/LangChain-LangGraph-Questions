"""
PRACTICAL CHALLENGE: LangGraph AgentState Definition (LC-H5-P07)
=====================================================
ID: LC-H5-P07
Curriculum Tier: Advanced | Focus: Tool Calling & LangGraph Basics
Task:
Define an `AgentState` schema using `TypedDict` containing `messages` (list of messages)
and `sender` (str) metadata.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from typing import TypedDict, List, Any

class AgentState(TypedDict):
    messages: List[Any]
    sender: str

def create_initial_state(user_text: str) -> AgentState:
    return {
        "messages": [{"role": "user", "content": user_text}],
        "sender": "user"
    }

def test_agent_state():
    state = create_initial_state("Analyze stock performance")
    assert state["sender"] == "user"
    assert len(state["messages"]) == 1
    assert state["messages"][0]["content"] == "Analyze stock performance"

if __name__ == '__main__':
    test_agent_state()
    print("✓ Task 07 passed!")
