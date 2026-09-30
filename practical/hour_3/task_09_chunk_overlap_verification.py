"""
PRACTICAL CHALLENGE: Sliding Window Chunk Overlap (LC-H3-P09)
=====================================================
ID: LC-H3-P09
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a sliding window chunk generator `sliding_window_chunks(words, window_size, overlap)`
and assert that successive chunks share exactly `overlap` words.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
def sliding_window_chunks(words: list, window_size: int, overlap: int) -> list:
    if overlap >= window_size:
        raise ValueError("Overlap must be strictly smaller than window_size.")
    step = window_size - overlap
    chunks = []
    for i in range(0, len(words), step):
        chunk = words[i:i + window_size]
        if chunk:
            chunks.append(chunk)
        if i + window_size >= len(words):
            break
    return chunks

def test_sliding_window():
    words = [f"word_{i}" for i in range(10)]
    chunks = sliding_window_chunks(words, window_size=4, overlap=2)

    assert len(chunks) == 4
    assert chunks[0] == ["word_0", "word_1", "word_2", "word_3"]
    assert chunks[1] == ["word_2", "word_3", "word_4", "word_5"]
    # Shared words between chunk 0 and chunk 1
    shared = set(chunks[0]).intersection(set(chunks[1]))
    assert len(shared) == 2

if __name__ == '__main__':
    test_sliding_window()
    print("✓ Task 09 passed!")
