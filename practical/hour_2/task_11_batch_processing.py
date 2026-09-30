"""
PRACTICAL CHALLENGE: Batch Invocation Support (LC-H2-P11)
=====================================================
ID: LC-H2-P11
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement batch execution on runnables maintaining item ordering.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class BatchableRunnable:
    def __init__(self, transform_fn):
        self.transform_fn = transform_fn

    def invoke(self, item):
        return self.transform_fn(item)

    def batch(self, items: list) -> list:
        return [self.invoke(item) for item in items]

def test_batch():
    runnable = BatchableRunnable(lambda text: f"Processed: {text.title()}")
    inputs = ["langchain", "prompt template", "vector database"]
    outputs = runnable.batch(inputs)

    assert outputs == [
        "Processed: Langchain",
        "Processed: Prompt Template",
        "Processed: Vector Database"
    ]

if __name__ == '__main__':
    test_batch()
    print("✓ Task 11 passed!")
