"""
PRACTICAL CHALLENGE: Human-in-the-Loop Verification Intercept (LC-H7-P11)
=====================================================
ID: LC-H7-P11
Curriculum Tier: Mastery | Focus: Autonomous LangGraph RAG Agent
Task:
Implement `human_verification_intercept(state, user_approval=True, correction=None)`
that allows human intervention before saving or finalizing an action.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def human_verification_intercept(state: dict, user_approval: bool = True, correction: str = None) -> dict:
    if user_approval:
        state["approval_status"] = "APPROVED"
    else:
        state["approval_status"] = "REJECTED"
        if correction:
            state["messages"].append({"role": "human_feedback", "content": correction})
    return state

def test_human_intercept():
    s = {"messages": [{"role": "assistant", "content": "Drafting contract..."}]}
    res_app = human_verification_intercept(s, user_approval=True)
    assert res_app["approval_status"] == "APPROVED"

    res_rej = human_verification_intercept(s, user_approval=False, correction="Adjust clause 3")
    assert res_rej["approval_status"] == "REJECTED"
    assert res_rej["messages"][-1]["content"] == "Adjust clause 3"

if __name__ == '__main__':
    test_human_intercept()
    print("✓ Task 11 passed!")
