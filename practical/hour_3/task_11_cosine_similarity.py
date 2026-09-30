"""
PRACTICAL CHALLENGE: Cosine Similarity Function (LC-H3-P11)
=====================================================
ID: LC-H3-P11
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement `cosine_similarity(vec_a, vec_b)` returning the dot product divided by norms,
and handling zero vectors safely by returning 0.0.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
import math

def cosine_similarity(vec_a: list, vec_b: list) -> float:
    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must have identical dimensions.")
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)

def test_cosine_similarity():
    v1 = [1.0, 0.0, 0.0]
    v2 = [1.0, 0.0, 0.0]
    v3 = [0.0, 1.0, 0.0]

    assert abs(cosine_similarity(v1, v2) - 1.0) < 1e-6
    assert abs(cosine_similarity(v1, v3) - 0.0) < 1e-6

if __name__ == '__main__':
    test_cosine_similarity()
    print("✓ Task 11 passed!")
