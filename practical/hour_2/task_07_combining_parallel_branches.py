"""
PRACTICAL CHALLENGE: Synthesizing Parallel Outputs (LC-H2-P07)
=====================================================
ID: LC-H2-P07
Curriculum Tier: Intermediate | Focus: LCEL & Chain Composition
Task:
Implement an analysis pipeline synthesizing outputs from parallel branches into a unified summary.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def extract_sentiment(review: str) -> str:
    low = review.lower()
    if "good" in low or "great" in low or "love" in low:
        return "Positive"
    return "Negative"

def extract_topics(review: str) -> list:
    topics = []
    if "battery" in review.lower(): topics.append("battery")
    if "screen" in review.lower(): topics.append("screen")
    if "camera" in review.lower(): topics.append("camera")
    return topics

def synthesize_report(data: dict) -> str:
    return f"Review Sentiment: {data['sentiment']} | Mentioned Features: {', '.join(data['topics'])}"

def analyze_review(review_text: str) -> str:
    parallel_outputs = {
        "sentiment": extract_sentiment(review_text),
        "topics": extract_topics(review_text)
    }
    return synthesize_report(parallel_outputs)

def test_combining_parallel():
    review = "I love the screen resolution and battery life on this phone!"
    report = analyze_review(review)
    assert "Review Sentiment: Positive" in report
    assert "battery" in report and "screen" in report

if __name__ == '__main__':
    test_combining_parallel()
    print("✓ Task 07 passed!")
