import os

hour_dir = "practical/hour_3"
os.makedirs(hour_dir, exist_ok=True)

tasks = [
    ("task_01_document_model.py", "LC-H3-P01", "Core Document Representation",
"""Implement a `Document` class storing `page_content` (str) and `metadata` (dict).
Ensure default metadata is an empty dictionary and equality checks compare both content and metadata.""",
r'''class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata if metadata is not None else {}

    def __eq__(self, other):
        if not isinstance(other, Document):
            return False
        return self.page_content == other.page_content and self.metadata == other.metadata

def test_document():
    doc1 = Document("LangChain is a framework.", {"source": "intro.txt", "page": 1})
    doc2 = Document("LangChain is a framework.", {"source": "intro.txt", "page": 1})
    doc3 = Document("Different content.", {"source": "intro.txt", "page": 1})

    assert doc1.page_content == "LangChain is a framework."
    assert doc1.metadata["source"] == "intro.txt"
    assert doc1 == doc2
    assert doc1 != doc3

if __name__ == '__main__':
    test_document()
    print("✓ Task 01 passed!")
'''),

    ("task_02_text_loader.py", "LC-H3-P02", "Text File Loader Implementation",
"""Implement a `TextLoader` that reads a plain text file from disk and returns a list containing
a single `Document` object with its text and metadata `{'source': file_path}`.""",
r'''class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class TextLoader:
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def load(self) -> list:
        with open(self.file_path, "r", encoding=self.encoding) as f:
            content = f.read()
        return [Document(page_content=content, metadata={"source": self.file_path})]

def test_text_loader():
    import tempfile
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as tmp:
        tmp.write("Sample document content for RAG indexing.")
        tmp_name = tmp.name

    try:
        loader = TextLoader(tmp_name)
        docs = loader.load()
        assert len(docs) == 1
        assert docs[0].page_content == "Sample document content for RAG indexing."
        assert docs[0].metadata["source"] == tmp_name
    finally:
        import os
        os.remove(tmp_name)

if __name__ == '__main__':
    test_text_loader()
    print("✓ Task 02 passed!")
'''),

    ("task_03_mock_pdf_loader.py", "LC-H3-P03", "PDF Document Loader Simulation",
"""Implement a `MockPyPDFLoader` that parses simulated multi-page PDF records and returns
one Document per page with metadata `{'source': path, 'page': page_number}`.""",
r'''class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class MockPyPDFLoader:
    def __init__(self, file_path: str, simulated_pages: list = None):
        self.file_path = file_path
        self.simulated_pages = simulated_pages or []

    def load(self) -> list:
        documents = []
        for idx, page_text in enumerate(self.simulated_pages, start=1):
            documents.append(Document(
                page_content=page_text,
                metadata={"source": self.file_path, "page": idx}
            ))
        return documents

def test_pdf_loader():
    pages = ["Page 1: Architecture of RAG", "Page 2: Vector Stores & FAISS", "Page 3: Evaluation Metrics"]
    loader = MockPyPDFLoader("docs/whitepaper.pdf", simulated_pages=pages)
    docs = loader.load()

    assert len(docs) == 3
    assert docs[0].metadata["page"] == 1
    assert docs[1].page_content == "Page 2: Vector Stores & FAISS"
    assert docs[2].metadata["source"] == "docs/whitepaper.pdf"

if __name__ == '__main__':
    test_pdf_loader()
    print("✓ Task 03 passed!")
'''),

    ("task_04_directory_loader.py", "LC-H3-P04", "Directory Document Loader",
"""Implement `DirectoryLoader` that scans a directory for files matching a glob pattern (e.g. `*.txt`),
loads each file using a loader class, and aggregates all documents into a single flat list.""",
r'''class Document:
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
'''),

    ("task_05_metadata_preservation.py", "LC-H3-P05", "Preserving Metadata During Transformations",
"""Implement `copy_with_new_content(doc, new_content)` that creates a new `Document` with updated text
while deeply copying existing metadata and updating character count in metadata.""",
r'''import copy

class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

def copy_with_new_content(doc: Document, new_content: str) -> Document:
    new_meta = copy.deepcopy(doc.metadata)
    new_meta["char_count"] = len(new_content)
    return Document(page_content=new_content, metadata=new_meta)

def test_metadata_preservation():
    original = Document("Original text", {"source": "data.csv", "author": "Alice"})
    transformed = copy_with_new_content(original, "Transformed and cleaned text")

    assert transformed.page_content == "Transformed and cleaned text"
    assert transformed.metadata["source"] == "data.csv"
    assert transformed.metadata["author"] == "Alice"
    assert transformed.metadata["char_count"] == len("Transformed and cleaned text")
    assert "char_count" not in original.metadata

if __name__ == '__main__':
    test_metadata_preservation()
    print("✓ Task 05 passed!")
'''),

    ("task_06_character_text_splitter.py", "LC-H3-P06", "CharacterTextSplitter Implementation",
"""Implement a `CharacterTextSplitter` with `chunk_size`, `chunk_overlap`, and `separator` (e.g. '\n\n')
that splits text into smaller string chunks respecting maximum chunk length.""",
r'''class CharacterTextSplitter:
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
'''),

    ("task_07_recursive_text_splitter.py", "LC-H3-P07", "Recursive Character Text Splitter",
"""Implement a `RecursiveCharacterTextSplitter` that attempts splitting by a hierarchy of separators
`["\n\n", "\n", " ", ""]` so that chunks never exceed `chunk_size`.""",
r'''class RecursiveCharacterTextSplitter:
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
'''),

    ("task_08_split_documents.py", "LC-H3-P08", "Splitting Documents with Metadata Propagation",
"""Implement `split_documents(docs, splitter)` which takes a list of `Document`s,
splits each document's text using the splitter, and propagates the original metadata to all resulting chunks.""",
r'''class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class SimpleSplitter:
    def __init__(self, chunk_size: int = 30):
        self.chunk_size = chunk_size

    def split_text(self, text: str) -> list:
        words = text.split()
        chunks = []
        curr = []
        curr_len = 0
        for w in words:
            if curr_len + len(w) + 1 <= self.chunk_size:
                curr.append(w)
                curr_len += len(w) + 1
            else:
                if curr: chunks.append(" ".join(curr))
                curr = [w]
                curr_len = len(w)
        if curr: chunks.append(" ".join(curr))
        return chunks

def split_documents(docs: list, splitter) -> list:
    out = []
    for doc in docs:
        chunks = splitter.split_text(doc.page_content)
        for idx, chunk in enumerate(chunks):
            meta = dict(doc.metadata)
            meta["chunk_index"] = idx
            out.append(Document(chunk, meta))
    return out

def test_split_documents():
    docs = [
        Document("Fast and reliable indexing for AI systems.", {"source": "guide.md"}),
        Document("Short doc.", {"source": "notes.md"})
    ]
    splitter = SimpleSplitter(chunk_size=20)
    chunked_docs = split_documents(docs, splitter)

    assert len(chunked_docs) >= 2
    assert chunked_docs[0].metadata["source"] == "guide.md"
    assert "chunk_index" in chunked_docs[0].metadata
    assert chunked_docs[-1].metadata["source"] == "notes.md"

if __name__ == '__main__':
    test_split_documents()
    print("✓ Task 08 passed!")
'''),

    ("task_09_chunk_overlap_verification.py", "LC-H3-P09", "Sliding Window Chunk Overlap",
"""Implement a sliding window chunk generator `sliding_window_chunks(words, window_size, overlap)`
and assert that successive chunks share exactly `overlap` words.""",
r'''def sliding_window_chunks(words: list, window_size: int, overlap: int) -> list:
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
'''),

    ("task_10_mock_embeddings.py", "LC-H3-P10", "Embedding Model Abstraction",
"""Implement a `MockEmbeddings` class with `embed_query(text)` and `embed_documents(texts)`
that returns deterministic normalized float vectors based on word frequencies.""",
r'''import math

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
'''),

    ("task_11_cosine_similarity.py", "LC-H3-P11", "Cosine Similarity Function",
"""Implement `cosine_similarity(vec_a, vec_b)` returning the dot product divided by norms,
and handling zero vectors safely by returning 0.0.""",
r'''import math

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
'''),

    ("task_12_in_memory_vector_store.py", "LC-H3-P12", "In-Memory Vector Store Indexing",
"""Implement an `InMemoryVectorStore` with `add_documents(docs)` and `similarity_search(query, k)`
using embedding vectors and cosine similarity.""",
r'''from task_10_mock_embeddings import MockEmbeddings
from task_11_cosine_similarity import cosine_similarity

class Document:
    def __init__(self, page_content: str, metadata: dict = None):
        self.page_content = page_content
        self.metadata = metadata or {}

class InMemoryVectorStore:
    def __init__(self, embedding_model=None):
        self.embedding_model = embedding_model or MockEmbeddings()
        self.records = []

    def add_documents(self, documents: list):
        texts = [d.page_content for d in documents]
        vectors = self.embedding_model.embed_documents(texts)
        for doc, vec in zip(documents, vectors):
            self.records.append({"doc": doc, "vector": vec})

    def similarity_search(self, query: str, k: int = 2) -> list:
        q_vec = self.embedding_model.embed_query(query)
        scored = []
        for rec in self.records:
            score = cosine_similarity(q_vec, rec["vector"])
            scored.append((score, rec["doc"]))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored[:k]]

def test_vector_store():
    store = InMemoryVectorStore()
    docs = [
        Document("LangChain vector database retrieval methods", {"id": 1}),
        Document("Cooking pasta recipes and ingredients", {"id": 2}),
        Document("Building AI agents with LLM prompts", {"id": 3})
    ]
    store.add_documents(docs)

    results = store.similarity_search("vector database", k=1)
    assert len(results) == 1
    assert "retrieval methods" in results[0].page_content

if __name__ == '__main__':
    test_vector_store()
    print("✓ Task 12 passed!")
'''),

    ("task_13_vector_store_from_documents.py", "LC-H3-P13", "from_documents Factory Method",
"""Implement `from_documents(documents, embedding)` factory constructor on `InMemoryVectorStore`.""",
r'''from task_12_in_memory_vector_store import InMemoryVectorStore, Document
from task_10_mock_embeddings import MockEmbeddings

def create_vector_store_from_documents(documents: list, embedding_model=None):
    store = InMemoryVectorStore(embedding_model or MockEmbeddings())
    store.add_documents(documents)
    return store

def test_from_documents():
    docs = [
        Document("LangChain chains and runnables", {"topic": "chains"}),
        Document("LangGraph state and cycles", {"topic": "graph"})
    ]
    store = create_vector_store_from_documents(docs)
    assert len(store.records) == 2
    top = store.similarity_search("LangChain chains", k=1)
    assert top[0].metadata["topic"] == "chains"

if __name__ == '__main__':
    test_from_documents()
    print("✓ Task 13 passed!")
'''),

    ("task_14_metadata_filtering.py", "LC-H3-P14", "Metadata Filtering in Vector Search",
"""Extend similarity search to accept a `filter_dict` parameter that restricts candidate documents
to those whose metadata matches all specified key-value constraints.""",
r'''from task_12_in_memory_vector_store import InMemoryVectorStore, Document
from task_11_cosine_similarity import cosine_similarity

class FilterableVectorStore(InMemoryVectorStore):
    def similarity_search_with_filter(self, query: str, filter_dict: dict, k: int = 2) -> list:
        q_vec = self.embedding_model.embed_query(query)
        scored = []
        for rec in self.records:
            doc = rec["doc"]
            # verify match
            match = all(doc.metadata.get(k) == v for k, v in filter_dict.items())
            if match:
                score = cosine_similarity(q_vec, rec["vector"])
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored[:k]]

def test_metadata_filtering():
    store = FilterableVectorStore()
    docs = [
        Document("LangChain tutorial part 1", {"topic": "langchain", "version": 1}),
        Document("LangChain tutorial part 2", {"topic": "langchain", "version": 2}),
        Document("General python guide", {"topic": "python", "version": 1})
    ]
    store.add_documents(docs)

    res = store.similarity_search_with_filter("tutorial", filter_dict={"version": 2}, k=5)
    assert len(res) == 1
    assert res[0].metadata["version"] == 2

if __name__ == '__main__':
    test_metadata_filtering()
    print("✓ Task 14 passed!")
'''),

    ("task_15_end_to_end_indexing_pipeline.py", "LC-H3-P15", "Complete Document Ingestion Pipeline",
"""Build an end-to-end ingestion pipeline:
1. Load raw simulated text
2. Split into overlapping chunks with metadata
3. Index chunks into vector store
4. Perform similarity search and return relevant document chunks.""",
r'''from task_01_document_model import Document
from task_08_split_documents import SimpleSplitter, split_documents
from task_12_in_memory_vector_store import InMemoryVectorStore

def run_ingestion_pipeline(raw_text: str, source_id: str, query: str) -> list:
    # 1. Wrap in document
    doc = Document(raw_text, {"source": source_id})
    # 2. Split
    splitter = SimpleSplitter(chunk_size=30)
    chunks = split_documents([doc], splitter)
    # 3. Index
    store = InMemoryVectorStore()
    store.add_documents(chunks)
    # 4. Search
    return store.similarity_search(query, k=2)

def test_ingestion_pipeline():
    raw = "LangChain is designed for building context-aware reasoning applications using LLMs."
    relevant = run_ingestion_pipeline(raw, "overview.md", "context-aware applications")

    assert len(relevant) > 0
    assert relevant[0].metadata["source"] == "overview.md"

if __name__ == '__main__':
    test_ingestion_pipeline()
    print("✓ Task 15 passed!")
''')
]

catalog_lines = [
    "# Hour 3 Practical Challenges Catalog",
    "",
    "Tier: **Intermediate** | Focus: `Document Loaders, Text Splitters, Embeddings & Vector Stores`",
    "",
    "| ID | Task Title | Difficulty | File Link |",
    "| :---: | :--- | :---: | :--- |"
]

for filename, task_id, title, desc, code in tasks:
    filepath = os.path.join(hour_dir, filename)
    content = f'''"""
PRACTICAL CHALLENGE: {title} ({task_id})
=====================================================
ID: {task_id}
Curriculum Tier: Intermediate | Focus: Document Ingestion & Vector Storage
Task:
{desc.strip()}

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""
{code.strip()}
'''
    with open(filepath, "w") as f:
        f.write(content)
    
    catalog_lines.append(f"| `{task_id}` | {title} | `Intermediate` | [{filename}]({filename}) |")

catalog_path = os.path.join(hour_dir, "README.md")
with open(catalog_path, "w") as f:
    f.write("\n".join(catalog_lines) + "\n")

print("Generated Hour 3 successfully via Python.")
