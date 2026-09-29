"""
PRACTICAL CHALLENGE: CharacterTextSplitter Implementation (LC-H3-P06)
=====================================================
ID: LC-H3-P06
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `CharacterTextSplitter` with `chunk_size`, `chunk_overlap`, and `separator` (e.g. '

')
that splits text into smaller string chunks respecting maximum chunk length.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class CharacterTextSplitter:
    def __init__(self, chunk_size: int = 100, chunk_overlap: int = 20, separator: str = "\n\n"):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator

    def split_text(self, text: str) -> list:
        paragraphs = text.split(self.separator)
        chunks = []
        current_chunk = ""

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            if not current_chunk:
                current_chunk = para
            elif len(current_chunk) + len(self.separator) + len(para) <= self.chunk_size:
                current_chunk += self.separator + para
            else:
                chunks.append(current_chunk)
                current_chunk = para

        if current_chunk:
            chunks.append(current_chunk)
        return chunks

def test_character_splitter():
    splitter = CharacterTextSplitter(chunk_size=50, separator="\n\n")
    sample = "First paragraph here.\n\nSecond paragraph is longer.\n\nThird paragraph."
    chunks = splitter.split_text(sample)

    assert len(chunks) >= 2
    assert "First paragraph here." in chunks[0]
    assert all(len(c) <= 50 for c in chunks)

if __name__ == '__main__':
    test_character_splitter()
    print("✓ Task 06 passed!")
