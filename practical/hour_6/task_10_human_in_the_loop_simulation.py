"""
PRACTICAL CHALLENGE: Simulating Human Review Interruption (LC-H6-P10)
=====================================================
ID: LC-H6-P10
Curriculum Tier: Advanced | Focus: LangGraph Loops & Document Crafter Agent
Task:
Implement a review handler `human_review_step(state, approved=True, feedback='')` that either
routes to save if approved, or loops back to update node with human feedback.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def human_review_step(state: dict, approved: bool, feedback: str = "") -> dict:
    if approved:
        return {"next_step": "save", "review_status": "APPROVED"}
    else:
        return {
            "next_step": "update",
            "review_status": "REVISE",
            "messages": state.get("messages", []) + [{"role": "user", "content": f"Please revise: {feedback}"}]
        }

def test_human_review():
    state = {"messages": [{"role": "ai", "content": "Draft v1"}]}
    
    # User rejects draft with feedback
    rev = human_review_step(state, approved=False, feedback="Tone is too casual")
    assert rev["next_step"] == "update"
    assert "Tone is too casual" in rev["messages"][-1]["content"]

    # User approves
    app = human_review_step(state, approved=True)
    assert app["next_step"] == "save"
    assert app["review_status"] == "APPROVED"

if __name__ == '__main__':
    test_human_review()
    print("✓ Task 10 passed!")
