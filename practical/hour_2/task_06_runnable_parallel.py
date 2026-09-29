"""
PRACTICAL CHALLENGE: RunnableParallel Concurrent Mapping (LC-H2-P06)
=====================================================
ID: LC-H2-P06
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement RunnableParallel for concurrent branch execution.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class RunnableParallel:
    def __init__(self, branches: dict):
        self.branches = branches

    def invoke(self, input_val) -> dict:
        results = {}
        for key, runnable in self.branches.items():
            results[key] = runnable(input_val) if callable(runnable) else runnable.invoke(input_val)
        return results

def test_runnable_parallel():
    parallel = RunnableParallel({
        "length": lambda text: len(text),
        "words": lambda text: len(text.split()),
        "first_word": lambda text: text.split()[0] if text.split() else ""
    })

    out = parallel.invoke("LangChain simplifies AI engineering")
    assert out["length"] == len("LangChain simplifies AI engineering")
    assert out["words"] == 4
    assert out["first_word"] == "LangChain"

if __name__ == '__main__':
    test_runnable_parallel()
    print("✓ Task 06 passed!")
