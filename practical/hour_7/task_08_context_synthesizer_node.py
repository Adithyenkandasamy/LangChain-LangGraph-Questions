"""
PRACTICAL CHALLENGE: Context Synthesis & Final Response Node (LC-H7-P08)
=====================================================
ID: LC-H7-P08
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `synthesize_answer_node(state)` that takes retrieved tool outputs and
formats a comprehensive synthesized answer citing the source context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def synthesize_answer_node(state: dict) -> dict:
    tool_msgs = [m for m in state.get("messages", []) if m.get("role") == "tool"]
    user_msgs = [m for m in state.get("messages", []) if m.get("role") == "user"]

    query = user_msgs[-1]["content"] if user_msgs else "unknown"
    if tool_msgs:
        context_parts = [m["content"] for m in tool_msgs]
        combined_context = " | ".join(context_parts)
        answer = f"Based on retrieved facts ({combined_context}), here is the answer for: {query}"
    else:
        answer = f"Direct response for: {query}"

    state["messages"].append({"role": "assistant", "content": answer})
    state["is_complete"] = True
    return state

def test_synthesizer():
    state = {
        "messages": [
            {"role": "user", "content": "Explain LangGraph"},
            {"role": "tool", "content": "LangGraph is stateful"}
        ],
        "is_complete": False
    }
    updated = synthesize_answer_node(state)
    assert updated["is_complete"] is True
    assert "Based on retrieved facts" in updated["messages"][-1]["content"]

if __name__ == '__main__':
    test_synthesizer()
    print("✓ Task 08 passed!")
