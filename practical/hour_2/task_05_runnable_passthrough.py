"""
PRACTICAL CHALLENGE: RunnablePassthrough Identity Function (LC-H2-P05)
=====================================================
ID: LC-H2-P05
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement RunnablePassthrough and RunnablePassthrough.assign for context passing.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class RunnablePassthrough:
    def invoke(self, x):
        return x

    @classmethod
    def assign(cls, **extra_fns):
        return RunnableAssign(extra_fns)

class RunnableAssign:
    def __init__(self, fns: dict):
        self.fns = fns

    def invoke(self, input_dict: dict) -> dict:
        result = dict(input_dict)
        for key, fn in self.fns.items():
            result[key] = fn(result)
        return result

def test_runnable_passthrough():
    passthrough = RunnablePassthrough()
    assert passthrough.invoke({"query": "AI"}) == {"query": "AI"}

    assigner = RunnablePassthrough.assign(
        word_count=lambda d: len(d["text"].split()),
        upper_text=lambda d: d["text"].upper()
    )
    res = assigner.invoke({"text": "hello langchain developers"})
    assert res["word_count"] == 3
    assert res["upper_text"] == "HELLO LANGCHAIN DEVELOPERS"
    assert res["text"] == "hello langchain developers"

if __name__ == '__main__':
    test_runnable_passthrough()
    print("✓ Task 05 passed!")
