"""
PRACTICAL CHALLENGE: RAG Agent State Schema with Reducer (LC-H7-P04)
=====================================================
ID: LC-H7-P04
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Define `AgentState` schema dictionary structure with `messages`, `retrieved_docs`,
and a reducer function `messages_reducer(existing, new_messages)` that appends messages.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def messages_reducer(existing: list, new_messages: list) -> list:
    combined = list(existing)
    for msg in new_messages:
        combined.append(msg)
    return combined

def create_initial_state(user_query: str) -> dict:
    return {
        "messages": [{"role": "user", "content": user_query}],
        "retrieved_docs": [],
        "iterations": 0,
        "is_complete": False
    }

def test_state_schema():
    s = create_initial_state("What is LangGraph?")
    assert s["iterations"] == 0
    assert len(s["messages"]) == 1
    updated_messages = messages_reducer(s["messages"], [{"role": "assistant", "content": "LangGraph is stateful."}])
    assert len(updated_messages) == 2

if __name__ == '__main__':
    test_state_schema()
    print("✓ Task 04 passed!")
