"""
PRACTICAL CHALLENGE: RAG Output Accuracy & Grounding Evaluator (LC-H4-P15)
=====================================================
ID: LC-H4-P15
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement an evaluation harness `evaluate_grounding(answer, context)` that verifies
whether answer key terms are grounded in the retrieved context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def evaluate_grounding(answer: str, context: str) -> dict:
    ans_words = set(w.lower() for w in answer.split() if len(w) > 4)
    ctx_words = set(w.lower() for w in context.split() if len(w) > 4)

    grounded_words = ans_words.intersection(ctx_words)
    ratio = len(grounded_words) / len(ans_words) if ans_words else 1.0

    return {
        "is_grounded": ratio >= 0.5,
        "grounding_ratio": round(ratio, 2),
        "grounded_terms": sorted(list(grounded_words))
    }

def test_grounding_evaluator():
    ctx = "The LangChain framework enables modular chain construction."
    ans_good = "LangChain enables modular construction."
    ans_hallucination = "Quantum computing relies on superconductors and qubits."

    res_good = evaluate_grounding(ans_good, ctx)
    assert res_good["is_grounded"] is True
    assert "langchain" in res_good["grounded_terms"]

    res_bad = evaluate_grounding(ans_hallucination, ctx)
    assert res_bad["is_grounded"] is False

if __name__ == '__main__':
    test_grounding_evaluator()
    print("✓ Task 15 passed!")
