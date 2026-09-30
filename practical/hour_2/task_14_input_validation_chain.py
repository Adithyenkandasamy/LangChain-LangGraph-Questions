"""
PRACTICAL CHALLENGE: Validating Inputs in LCEL Pipeline (LC-H2-P14)
=====================================================
ID: LC-H2-P14
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement pre-execution input validator ensuring required dictionary keys are provided.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class InputValidator:
    def __init__(self, required_keys: set):
        self.required_keys = required_keys

    def invoke(self, inputs: dict) -> dict:
        missing = self.required_keys - set(inputs.keys())
        if missing:
            raise ValueError(f"Missing required input keys: {sorted(list(missing))}")
        return inputs

def test_input_validation_chain():
    validator = InputValidator(required_keys={"topic", "language"})
    valid_input = {"topic": "Async IO", "language": "Python", "extra": 123}
    assert validator.invoke(valid_input) == valid_input

    try:
        validator.invoke({"topic": "Async IO"})
        assert False, "Should fail on missing 'language'"
    except ValueError as e:
        assert "language" in str(e)

if __name__ == '__main__':
    test_input_validation_chain()
    print("✓ Task 14 passed!")
