"""
PRACTICAL CHALLENGE: Resilient Chains with Fallbacks (LC-H2-P09)
=====================================================
ID: LC-H2-P09
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement a fallback runner that recovers gracefully when primary step encounters exceptions.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class FallbackRunner:
    def __init__(self, primary, fallbacks: list):
        self.primary = primary
        self.fallbacks = fallbacks

    def invoke(self, input_val):
        try:
            return self.primary(input_val)
        except Exception:
            for fb in self.fallbacks:
                try:
                    return fb(input_val)
                except Exception:
                    continue
            raise RuntimeError("All fallbacks failed.")

def test_fallbacks():
    failing_primary = lambda x: 1 / 0
    secondary_fail = lambda x: [][5]
    successful_fallback = lambda x: f"Recovered with: {x}"

    runner = FallbackRunner(failing_primary, [secondary_fail, successful_fallback])
    res = runner.invoke("TestInput")
    assert res == "Recovered with: TestInput"

if __name__ == '__main__':
    test_fallbacks()
    print("✓ Task 09 passed!")
