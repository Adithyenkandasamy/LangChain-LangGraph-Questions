"""
PRACTICAL CHALLENGE: Recursive Character Text Splitter (LC-H3-P07)
=====================================================
ID: LC-H3-P07
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement a `RecursiveCharacterTextSplitter` that attempts splitting by a hierarchy of separators
`["

", "
", " ", ""]` so that chunks never exceed `chunk_size`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class RecursiveCharacterTextSplitter:
    def __init__(self, chunk_size: int = 40, chunk_overlap: int = 10):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = ["\n\n", "\n", " ", ""]

    def split_text(self, text: str) -> list:
        def _split(txt, seps):
            if len(txt) <= self.chunk_size or not seps:
                return [txt] if txt else []
            sep = seps[0]
            parts = txt.split(sep) if sep else list(txt)
            result = []
            curr = ""
            for p in parts:
                candidate = curr + (sep if curr and sep else "") + p
                if len(candidate) <= self.chunk_size:
                    curr = candidate
                else:
                    if curr:
                        result.append(curr)
                    if len(p) > self.chunk_size:
                        result.extend(_split(p, seps[1:]))
                        curr = ""
                    else:
                        curr = p
            if curr:
                result.append(curr)
            return result

        return _split(text, self.separators)

def test_recursive_splitter():
    splitter = RecursiveCharacterTextSplitter(chunk_size=30)
    text = "LangChain is great.\n\nIt supports modular chains and graphs.\nPowerful tooling."
    chunks = splitter.split_text(text)

    assert len(chunks) >= 2
    assert all(len(c) <= 30 for c in chunks)

if __name__ == '__main__':
    test_recursive_splitter()
    print("✓ Task 07 passed!")
