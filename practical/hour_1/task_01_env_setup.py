"""
PRACTICAL CHALLENGE: Environment Configuration & API Key Loader (LC-H1-P01)
=====================================================
ID: LC-H1-P01
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Define a function `load_gemini_credentials(env_dict=None)` that loads and verifies the `GOOGLE_API_KEY`.
It should validate that the key exists, is non-empty, and does not contain whitespace.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import os

def load_gemini_credentials(env_dict=None):
    if env_dict is not None:
        key = env_dict.get("GOOGLE_API_KEY")
    else:
        key = os.getenv("GOOGLE_API_KEY")
    
    if not key or not isinstance(key, str) or not key.strip():
        raise ValueError("GOOGLE_API_KEY must be a non-empty string.")
    
    clean_key = key.strip()
    return {"GOOGLE_API_KEY": clean_key}

def test_credentials():
    # Valid key
    creds = load_gemini_credentials({"GOOGLE_API_KEY": "AIzaSyFakeKey123"})
    assert creds["GOOGLE_API_KEY"] == "AIzaSyFakeKey123"

    # Missing key raises ValueError
    try:
        load_gemini_credentials({})
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "GOOGLE_API_KEY" in str(e)

    # Empty key raises ValueError
    try:
        load_gemini_credentials({"GOOGLE_API_KEY": "   "})
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "GOOGLE_API_KEY" in str(e)

if __name__ == '__main__':
    test_credentials()
    print("✓ Task 01 passed!")
