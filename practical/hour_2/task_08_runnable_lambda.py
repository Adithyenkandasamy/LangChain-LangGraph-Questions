"""
PRACTICAL CHALLENGE: RunnableLambda Custom Transformations (LC-H2-P08)
=====================================================
ID: LC-H2-P08
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement RunnableLambda to convert any Python callable into a pipeable Runnable.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class RunnableLambda:
    def __init__(self, func):
        self.func = func

    def invoke(self, input_val):
        return self.func(input_val)

    def __or__(self, other):
        return RunnableLambda(lambda x: other.invoke(self.invoke(x)))

def test_runnable_lambda():
    double_fn = RunnableLambda(lambda x: x * 2)
    add_five = RunnableLambda(lambda x: x + 5)
    to_string = RunnableLambda(lambda x: f"Result: {x}")

    chain = double_fn | add_five | to_string
    assert chain.invoke(10) == "Result: 25"

if __name__ == '__main__':
    test_runnable_lambda()
    print("✓ Task 08 passed!")
