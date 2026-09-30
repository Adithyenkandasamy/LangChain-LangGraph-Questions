"""
PRACTICAL CHALLENGE: Threshold-Based Retrieval (LC-H4-P02)
=====================================================
ID: LC-H4-P02
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement a retriever that filters out documents with similarity score below `score_threshold`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class ThresholdRetriever:
    def __init__(self, documents_with_scores: list, score_threshold: float = 0.7):
        self.data = documents_with_scores
        self.score_threshold = score_threshold

    def invoke(self, query: str) -> list:
        # returns docs that meet threshold
        return [doc for doc, score in self.data if score >= self.score_threshold]

def test_threshold_retriever():
    data = [
        ("Doc 1: Exact Match", 0.95),
        ("Doc 2: Moderate Match", 0.72),
        ("Doc 3: Low Match", 0.45)
    ]
    retriever = ThresholdRetriever(data, score_threshold=0.7)
    passed_docs = retriever.invoke("Match")

    assert len(passed_docs) == 2
    assert "Doc 1: Exact Match" in passed_docs
    assert "Doc 2: Moderate Match" in passed_docs
    assert "Doc 3: Low Match" not in passed_docs

if __name__ == '__main__':
    test_threshold_retriever()
    print("✓ Task 02 passed!")
