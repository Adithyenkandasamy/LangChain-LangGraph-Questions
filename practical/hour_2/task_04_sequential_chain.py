"""
PRACTICAL CHALLENGE: Two-Stage Sequential Chain (LC-H2-P04)
=====================================================
ID: LC-H2-P04
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement a two-stage sequential chain where stage 1 output feeds into stage 2 input.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class OutlineGenerator:
    def invoke(self, inputs: dict) -> dict:
        topic = inputs["topic"]
        return {"outline": f"1. Intro to {topic}\n2. Core Mechanisms\n3. Future Trends"}

class SummaryGenerator:
    def invoke(self, inputs: dict) -> str:
        outline = inputs["outline"]
        return f"Summary of points:\n- {outline.replace(chr(10), ' | ')}"

class SequentialChain:
    def __init__(self, stage1, stage2):
        self.stage1 = stage1
        self.stage2 = stage2

    def invoke(self, inputs: dict) -> str:
        s1_out = self.stage1.invoke(inputs)
        return self.stage2.invoke(s1_out)

def test_sequential_chain():
    chain = SequentialChain(OutlineGenerator(), SummaryGenerator())
    res = chain.invoke({"topic": "LangGraph"})
    assert "Summary of points:" in res
    assert "1. Intro to LangGraph" in res
    assert "3. Future Trends" in res

if __name__ == '__main__':
    test_sequential_chain()
    print("✓ Task 04 passed!")
