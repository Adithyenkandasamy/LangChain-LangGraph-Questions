"""
PRACTICAL CHALLENGE: Dynamic Branch Routing (RunnableBranch) (LC-H2-P10)
=====================================================
ID: LC-H2-P10
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement RunnableBranch to direct input dynamically to matching logic handler.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class RunnableBranch:
    def __init__(self, branches: list, default_branch):
        self.branches = branches
        self.default_branch = default_branch

    def invoke(self, input_val):
        for condition_fn, runnable in self.branches:
            if condition_fn(input_val):
                return runnable(input_val)
        return self.default_branch(input_val)

def test_conditional_branch():
    branch = RunnableBranch(
        branches=[
            (lambda x: x["category"] == "math", lambda x: f"Math: {eval(x['query'])}"),
            (lambda x: x["category"] == "greet", lambda x: f"Greeting: Hello {x['name']}!")
        ],
        default_branch=lambda x: f"General query: {x.get('query', '')}"
    )

    assert branch.invoke({"category": "math", "query": "2 + 3"}) == "Math: 5"
    assert branch.invoke({"category": "greet", "name": "Alice"}) == "Greeting: Hello Alice!"
    assert branch.invoke({"category": "other", "query": "weather today"}) == "General query: weather today"

if __name__ == '__main__':
    test_conditional_branch()
    print("✓ Task 10 passed!")
