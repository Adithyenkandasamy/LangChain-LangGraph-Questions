"""
PRACTICAL CHALLENGE: Maximal Marginal Relevance (MMR) Retrieval (LC-H4-P03)
=====================================================
ID: LC-H4-P03
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement an MMR ranking function that balances query relevance and diversity among selected documents.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def mmr_rerank(query_score_map: dict, similarity_matrix: dict, lambda_mult: float = 0.5, k: int = 2) -> list:
    selected = []
    candidates = list(query_score_map.keys())

    while len(selected) < k and candidates:
        best_doc = None
        best_mmr_score = -float('inf')

        for c in candidates:
            sim_to_query = query_score_map[c]
            max_sim_to_selected = max([similarity_matrix.get((c, s), similarity_matrix.get((s, c), 0.0)) for s in selected], default=0.0)
            mmr = lambda_mult * sim_to_query - (1 - lambda_mult) * max_sim_to_selected
            if mmr > best_mmr_score:
                best_mmr_score = mmr
                best_doc = c

        if best_doc is not None:
            selected.append(best_doc)
            candidates.remove(best_doc)

    return selected

def test_mmr():
    query_scores = {"docA": 0.9, "docB": 0.88, "docC": 0.7}
    # docA and docB are near duplicates (sim 0.95), docC is diverse (sim 0.1)
    sim_matrix = {("docA", "docB"): 0.95, ("docA", "docC"): 0.1, ("docB", "docC"): 0.1}

    # High diversity (lambda = 0.2) should pick docA and docC rather than docB
    top_diverse = mmr_rerank(query_scores, sim_matrix, lambda_mult=0.2, k=2)
    assert top_diverse[0] == "docA"
    assert top_diverse[1] == "docC"

if __name__ == '__main__':
    test_mmr()
    print("✓ Task 03 passed!")
