"""
PRACTICAL CHALLENGE: Embedding Model Abstraction (LC-H3-P10)
=====================================================
ID: LC-H3-P10
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `MockEmbeddings` class with `embed_query(text)` and `embed_documents(texts)`
that returns deterministic normalized float vectors based on word frequencies.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import math

class MockEmbeddings:
    VOCAB = ["langchain", "vector", "database", "retrieval", "llm", "agent", "prompt"]

    def _embed(self, text: str) -> list:
        low = text.lower()
        vec = [float(low.count(term)) for term in self.VOCAB]
        norm = math.sqrt(sum(x*x for x in vec))
        if norm > 0:
            return [x / norm for x in vec]
        return [0.0] * len(self.VOCAB)

    def embed_query(self, text: str) -> list:
        return self._embed(text)

    def embed_documents(self, texts: list) -> list:
        return [self._embed(t) for t in texts]

def test_mock_embeddings():
    emb = MockEmbeddings()
    v1 = emb.embed_query("LangChain vector database retrieval")
    assert len(v1) == len(MockEmbeddings.VOCAB)
    # Check unit vector normalization
    magnitude = math.sqrt(sum(x*x for x in v1))
    assert abs(magnitude - 1.0) < 1e-4

    docs = emb.embed_documents(["LangChain agent", "LLM prompt"])
    assert len(docs) == 2

if __name__ == '__main__':
    test_mock_embeddings()
    print("✓ Task 10 passed!")
