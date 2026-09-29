"""
PRACTICAL CHALLENGE: Empty Retrieval Guard & Fallback Handler (LC-H7-P10)
=====================================================
ID: LC-H7-P10
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement a fallback handler `handle_empty_retrieval(state)`:
If the retriever returns no content or indicates failure, set state flag `fallback_used=True`
and generate a courteous notice that external data was unavailable.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def handle_empty_retrieval(state: dict) -> dict:
    last_msg = state["messages"][-1]
    if last_msg.get("role") == "tool" and ("no relevant" in last_msg.get("content", "").lower() or not last_msg.get("content")):
        state["fallback_used"] = True
        state["messages"].append({
            "role": "assistant",
            "content": "I could not find relevant documentation in the knowledge base. Answering from general knowledge."
        })
    else:
        state["fallback_used"] = False
    return state

def test_fallback():
    s1 = {"messages": [{"role": "tool", "content": "No relevant context found."}]}
    res1 = handle_empty_retrieval(s1)
    assert res1["fallback_used"] is True
    assert "could not find" in res1["messages"][-1]["content"]

    s2 = {"messages": [{"role": "tool", "content": "Found section 4.2"}]}
    res2 = handle_empty_retrieval(s2)
    assert res2["fallback_used"] is False

if __name__ == '__main__':
    test_fallback()
    print("✓ Task 10 passed!")
