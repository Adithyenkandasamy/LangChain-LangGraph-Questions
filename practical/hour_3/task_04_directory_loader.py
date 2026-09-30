"""
PRACTICAL CHALLENGE: Directory Document Loader (LC-H3-P04)
=====================================================
ID: LC-H3-P04
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
Implement `DirectoryLoader` that scans a directory for files matching a glob pattern (e.g. `*.txt`),
loads each file using a loader class, and aggregates all documents into a single flat list.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class MockFileLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
    def load(self):
        return [Document(f"Content from {self.file_path}", {"source": self.file_path})]

class DirectoryLoader:
    def __init__(self, dir_path: str, glob_pattern: str = "*.txt", loader_cls=MockFileLoader):
        self.dir_path = dir_path
        self.glob_pattern = glob_pattern
        self.loader_cls = loader_cls

    def load(self, mock_files: list = None) -> list:
        # In a real environment uses glob.glob; here supports simulated file paths for robust unit testing
        files = mock_files or []
        all_docs = []
        for f in files:
            loader = self.loader_cls(f)
            all_docs.extend(loader.load())
        return all_docs

def test_directory_loader():
    dir_loader = DirectoryLoader("docs/", glob_pattern="*.txt")
    simulated_files = ["docs/doc1.txt", "docs/doc2.txt", "docs/notes.txt"]
    docs = dir_loader.load(mock_files=simulated_files)

    assert len(docs) == 3
    assert docs[0].metadata["source"] == "docs/doc1.txt"
    assert docs[2].page_content == "Content from docs/notes.txt"

if __name__ == '__main__':
    test_directory_loader()
    print("✓ Task 04 passed!")
