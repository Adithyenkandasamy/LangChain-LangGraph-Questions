"""
PRACTICAL CHALLENGE: Prompt Composition Pipeline (LC-H1-P10)
=====================================================
ID: LC-H1-P10
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a prompt composer that joins a base system instruction with dynamic task instructions
and format constraints into a unified single prompt string.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def compose_prompt(system_role: str, user_task: str, formatting_constraint: str) -> str:
    parts = [
        f"### System Instructions:\n{system_role.strip()}",
        f"### User Task:\n{user_task.strip()}",
        f"### Output Format:\n{formatting_constraint.strip()}"
    ]
    return "\n\n".join(parts)

def test_prompt_composition():
    composed = compose_prompt(
        system_role="You are a senior Python architect.",
        user_task="Refactor this function for O(n) runtime.",
        formatting_constraint="Return valid Python code inside markdown blocks only."
    )
    assert "System Instructions:" in composed
    assert "senior Python architect" in composed
    assert "O(n) runtime" in composed
    assert "Output Format:" in composed

if __name__ == '__main__':
    test_prompt_composition()
    print("✓ Task 10 passed!")
