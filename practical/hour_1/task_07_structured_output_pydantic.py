"""
PRACTICAL CHALLENGE: Structured Output with Pydantic Schema (LC-H1-P07)
=====================================================
ID: LC-H1-P07
Curriculum Tier: Beginner | Focus: LangChain Setup & Prompts
Task:
Define a Pydantic model `ReportSummary` with fields `title` (str), `key_points` (list of str),
and `word_count` (int). Implement a parser `parse_report_json(json_str)` that validates and returns the instance.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
from pydantic import BaseModel, Field
import json

class ReportSummary(BaseModel):
    title: str = Field(description="The main title of the generated report")
    key_points: list[str] = Field(description="List of key points")
    word_count: int = Field(ge=0, description="Estimated total word count")

def parse_report_json(json_str: str) -> ReportSummary:
    data = json.loads(json_str)
    return ReportSummary.model_validate(data)

def test_structured_output():
    valid_json = '{"title": "AI in 2026", "key_points": ["LLMs everywhere", "Agent systems"], "word_count": 450}'
    report = parse_report_json(valid_json)
    assert report.title == "AI in 2026"
    assert len(report.key_points) == 2
    assert report.word_count == 450

    invalid_json = '{"title": "Broken", "key_points": "Not a list", "word_count": -5}'
    try:
        parse_report_json(invalid_json)
        assert False, "Should raise ValidationError"
    except Exception:
        pass

if __name__ == '__main__':
    test_structured_output()
    print("✓ Task 07 passed!")
