"""
PRACTICAL CHALLENGE: Runnable Pipe Operator Abstraction (LC-H2-P01)
=====================================================
ID: LC-H2-P01
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Define a `Runnable` base class supporting the `|` pipe operator to form sequential runnable pipelines.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Runnable:
    def __or__(self, other):
        return RunnableSequence(self, other)

    def invoke(self, input_val):
        raise NotImplementedError

class RunnableSequence(Runnable):
    def __init__(self, first: Runnable, second: Runnable):
        self.first = first
        self.second = second

    def invoke(self, input_val):
        intermediate = self.first.invoke(input_val)
        return self.second.invoke(intermediate)

class AddSuffix(Runnable):
    def __init__(self, suffix: str):
        self.suffix = suffix
    def invoke(self, input_val: str):
        return input_val + self.suffix

def test_pipe_operator():
    step1 = AddSuffix(" -> Step 1")
    step2 = AddSuffix(" -> Step 2")
    chain = step1 | step2
    result = chain.invoke("Start")
    assert result == "Start -> Step 1 -> Step 2"

if __name__ == '__main__':
    test_pipe_operator()
    print("✓ Task 01 passed!")
