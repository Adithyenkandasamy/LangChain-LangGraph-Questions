"""
PRACTICAL CHALLENGE: Injecting Citations into Answers (LC-H4-P06)
=====================================================
ID: LC-H4-P06
Curriculum Tier: Advanced | Focus: Advanced RAG & Tool Interfaces
Task:
Implement `append_citations(answer, sources)` which formats a list of unique source identifiers
and appends a '### Sources:' section at the bottom of the answer.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def append_citations(answer: str, sources: list) -> str:
    unique_sources = sorted(list(set(sources)))
    if not unique_sources:
        return answer.strip()
    sources_block = "\n\n### Sources:\n" + "\n".join(f"- {s}" for s in unique_sources)
    return answer.strip() + sources_block

def test_citations():
    raw_answer = "LangGraph enables stateful multi-agent workflows."
    with_sources = append_citations(raw_answer, ["intro.md", "guide.pdf", "intro.md"])

    assert "### Sources:" in with_sources
    assert "- guide.pdf" in with_sources
    assert "- intro.md" in with_sources
    # Verify deduplication (intro.md appears once)
    assert with_sources.count("intro.md") == 1

if __name__ == '__main__':
    test_citations()
    print("✓ Task 06 passed!")
