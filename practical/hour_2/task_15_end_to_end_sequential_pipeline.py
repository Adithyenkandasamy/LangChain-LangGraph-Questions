"""
PRACTICAL CHALLENGE: Complete End-to-End Multi-Step Pipeline (LC-H2-P15)
=====================================================
ID: LC-H2-P15
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Build a complete multi-stage text processing pipeline with cleaning, validation, and summarization.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ArticlePipeline:
    def __init__(self):
        pass

    def run(self, inputs: dict) -> dict:
        if "raw_text" not in inputs:
            raise KeyError("Input must contain 'raw_text'")
        cleaned = " ".join(inputs["raw_text"].strip().split())
        summary = f"Summary: {cleaned[:40]}..."
        return {
            "original_length": len(inputs["raw_text"]),
            "cleaned_text": cleaned,
            "summary": summary,
            "status": "PROCESSED"
        }

def test_end_to_end_pipeline():
    pipeline = ArticlePipeline()
    payload = {"raw_text": "   LangChain   Expression    Language enables easy composition of chains.   "}
    result = pipeline.run(payload)

    assert result["status"] == "PROCESSED"
    assert result["cleaned_text"] == "LangChain Expression Language enables easy composition of chains."
    assert "Summary: LangChain Expression Language enables ea..." == result["summary"]

if __name__ == '__main__':
    test_end_to_end_pipeline()
    print("✓ Task 15 passed!")
