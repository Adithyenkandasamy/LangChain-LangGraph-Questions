"""
PRACTICAL CHALLENGE: Catching Schema Validation Errors (LC-H1-P12)
=====================================================
ID: LC-H1-P12
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Implement a safe parser `safe_parse_json(json_str, schema_cls)` that returns a tuple `(instance, error_message)`.
If parsing succeeds, error_message is None; if it fails, instance is None and error_message contains details.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from pydantic import BaseModel, ValidationError
import json

class SentimentOutput(BaseModel):
    sentiment: str
    confidence: float

def safe_parse_json(json_str: str, schema_cls):
    try:
        data = json.loads(json_str)
        instance = schema_cls.model_validate(data)
        return (instance, None)
    except (json.JSONDecodeError, ValidationError, Exception) as e:
        return (None, str(e))

def test_safe_parse():
    success_json = '{"sentiment": "positive", "confidence": 0.95}'
    inst, err = safe_parse_json(success_json, SentimentOutput)
    assert inst is not None and err is None
    assert inst.sentiment == "positive"
    assert inst.confidence == 0.95

    fail_json = '{"sentiment": "positive", "confidence": "high"}'
    inst, err = safe_parse_json(fail_json, SentimentOutput)
    assert inst is None and err is not None

if __name__ == '__main__':
    test_safe_parse()
    print("✓ Task 12 passed!")
