"""
PRACTICAL CHALLENGE: Grounded RAG Prompt Builder (LC-H4-P05)
=====================================================
ID: LC-H4-P05
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Build a prompt generator that explicitly instructs the LLM:
'Answer the question based ONLY on the context below. If you cannot find the answer, reply "I do not know".'

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def create_rag_prompt(context: str, question: str) -> str:
    template = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you do not know the answer based on "
        "the provided context, reply exactly with 'I do not know'. Do not hallucinate.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )
    return template

def test_rag_prompt():
    prompt = create_rag_prompt("RAG stands for Retrieval-Augmented Generation.", "What does RAG mean?")
    assert "retrieved context" in prompt
    assert "'I do not know'" in prompt
    assert "What does RAG mean?" in prompt

if __name__ == '__main__':
    test_rag_prompt()
    print("✓ Task 05 passed!")
