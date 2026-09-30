"""
PRACTICAL CHALLENGE: Model Configuration & Temperature Validation (LC-H1-P11)
=====================================================
ID: LC-H1-P11
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a `ModelConfig` class that validates temperature bounds (must be between 0.0 and 2.0)
and validates model name against supported Gemini models (`gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ModelConfig:
    SUPPORTED_MODELS = {"gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"}

    def __init__(self, model: str, temperature: float = 0.7, max_tokens: int = 1000):
        if model not in self.SUPPORTED_MODELS:
            raise ValueError(f"Model '{model}' is not supported. Choose from {self.SUPPORTED_MODELS}")
        if not (0.0 <= temperature <= 2.0):
            raise ValueError("Temperature must be between 0.0 and 2.0")
        if max_tokens <= 0:
            raise ValueError("max_tokens must be positive")

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

def test_model_config():
    cfg = ModelConfig("gemini-1.5-flash", temperature=0.5, max_tokens=500)
    assert cfg.model == "gemini-1.5-flash"
    assert cfg.temperature == 0.5

    try:
        ModelConfig("unknown-model")
        assert False, "Should raise ValueError for unsupported model"
    except ValueError:
        pass

    try:
        ModelConfig("gemini-1.5-flash", temperature=2.5)
        assert False, "Should raise ValueError for temperature > 2.0"
    except ValueError:
        pass

if __name__ == '__main__':
    test_model_config()
    print("✓ Task 11 passed!")
