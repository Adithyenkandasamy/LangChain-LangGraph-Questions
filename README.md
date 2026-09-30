# LangChain & LangGraph Questions & Practice Repository

A comprehensive, structured curriculum of **420 Individual Theory Question Files** and **105 Practical Python Challenge Files** based directly on the comprehensive ~7-hour course tutorial covering LangChain and LangGraph from foundations to autonomous multi-agent systems.

> 📺 **Course Reference**: [Transcription.md](Transcription.md) (Full 6h 49m In-Depth Lecture & Code)  
> 💡 **Solutions Reference**: Companion solutions with in-depth technical explanations and code walkthroughs  
> 🎯 **Design Methodology**: 100% Zero-Spoiler modular architecture modeled after the standard curriculum format  

---

## 🗂️ Curriculum Overview: Theory & Practical per Hour

| Hour & Course Chapters | Timestamp Range | Theory Questions (60/hr) | Master Catalog | Practical Challenges (15/hr) | Core Focus & Concepts |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Hour 1**: Foundations, Setup & Prompt Templates | `00:00:00` – `01:00:00` | [📝 Hour 1 Directory](theory/hour_1/) | [📖 Hour 1 Catalog](theory/hour_1.md) | [💻 Tasks 01–15](practical/hour_1/) | Gemini Flash, environment setup, message primitives (`HumanMessage`, `AIMessage`, `SystemMessage`), prompt templates, `MessagesPlaceholder`, TypedDict & Pydantic structured output. |
| **Hour 2**: Output Parsers & LCEL Chains | `01:00:00` – `02:00:00` | [📝 Hour 2 Directory](theory/hour_2/) | [📖 Hour 2 Catalog](theory/hour_2.md) | [💻 Tasks 16–30](practical/hour_2/) | `StrOutputParser`, `StructuredOutputParser`, `PydanticOutputParser`, `OutputFixingParser`, LCEL pipe (`\|`) syntax, `RunnableSequence`, `RunnableBranch`, `RunnableParallel`. |
| **Hour 3**: Embeddings, Text Splitting & Loaders | `02:00:00` – `03:00:00` | [📝 Hour 3 Directory](theory/hour_3/) | [📖 Hour 3 Catalog](theory/hour_3.md) | [💻 Tasks 31–45](practical/hour_3/) | Dense embeddings (`all-MiniLM-L6-v2`), cosine similarity, `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, `PyPDFLoader`, `DirectoryLoader`, `WebBaseLoader`, `CSVLoader`, Chroma vector store. |
| **Hour 4**: Retrievers, Context Injection & Tools | `03:00:00` – `04:00:00` | [📝 Hour 4 Directory](theory/hour_4/) | [📖 Hour 4 Catalog](theory/hour_4.md) | [💻 Tasks 46–60](practical/hour_4/) | `as_retriever()`, MMR algorithm, `WikipediaRetriever`, context stuffing, end-to-end LCEL RAG chains, `@tool` decorator, docstrings, type annotations, multi-tool registration. |
| **Hour 5**: Tool Binding, Execution & LangGraph Intro | `04:00:00` – `05:00:00` | [📝 Hour 5 Directory](theory/hour_5/) | [📖 Hour 5 Catalog](theory/hour_5.md) | [💻 Tasks 61–75](practical/hour_5/) | `model.bind_tools()`, `AIMessage.tool_calls`, `ToolMessage`, multi-step tool execution loops (currency converter), StateGraph basics, `START`, `END`, state typing. |
| **Hour 6**: LangGraph Conditional Edges & Cycles | `05:00:00` – `06:00:00` | [📝 Hour 6 Directory](theory/hour_6/) | [📖 Hour 6 Catalog](theory/hour_6.md) | [💻 Tasks 76–90](practical/hour_6/) | `add_conditional_edges`, router functions, cyclic graph loops (number guessing loop), loop safeguards, `add_messages` reducer, LangGraph message state with Gemini. |
| **Hour 7**: Autonomous Agents (Doc Editor & RAG Agent) | `06:00:00` – `06:49:41` | [📝 Hour 7 Directory](theory/hour_7/) | [📖 Hour 7 Catalog](theory/hour_7.md) | [💻 Tasks 91–105](practical/hour_7/) | Document Crafter / Email Drafter Agent, autonomous RAG Agent with LangGraph, PDF ingestion, Chroma retrieval tool, `ToolNode`, `tools_condition`, fallbacks, streaming. |

---

## 📂 Repository Architecture

```text
LangChain-LangGraph-Questions/
├── README.md                      # Master curriculum index and repository guide
├── Transcription.md               # Complete course lecture and code transcript (6h 49m)
├── theory/
│   ├── hour_1/ to hour_7/         # 420 individual markdown files (q01_....md to q60_....md)
│   ├── hour_1.md to hour_7.md     # Master catalog files indexing each hour's 60 questions
│   └── hour_1/README.md to hour_7/README.md
└── practical/
    ├── hour_1/                    # Tasks 01–15: Environment, messages, templates, structured output
    ├── hour_2/                    # Tasks 16–30: Output parsers, LCEL, branches, parallel chains
    ├── hour_3/                    # Tasks 31–45: Embeddings, splitters, PDF/Web/CSV loaders, ChromaDB
    ├── hour_4/                    # Tasks 46–60: Retrievers, MMR, Wikipedia, LCEL RAG, @tool definitions
    ├── hour_5/                    # Tasks 61–75: bind_tools, tool_calls, ToolMessage, StateGraph basics
    ├── hour_6/                    # Tasks 76–90: Conditional routing, cyclic loops, add_messages reducer
    ├── hour_7/                    # Tasks 91–105: Autonomous RAG agent, PDF ingestion, ToolNode, fallbacks
    └── hour_1/README.md to hour_7/README.md
```

---

## 🎯 How to Use This Repository

### 1. Theory Practice (Zero Spoilers)
- Navigate into any hour folder under [`theory/`](theory/), e.g. [`theory/hour_1/`](theory/hour_1/).
- Open any individual question file (e.g. [`q01_framework_classification.md`](theory/hour_1/q01_framework_classification.md)) to test your conceptual mastery.
- Every question file is isolated and contains **zero spoiler answers**.
- You can browse the full hour catalogs in [`theory/hour_1.md`](theory/hour_1.md) through [`theory/hour_7.md`](theory/hour_7.md) for an overview of all topics and difficulty tiers.

### 2. Practical Python Challenges
- Every task under [`practical/`](practical/) is a standalone, runnable Python challenge with an embedded assertion suite.
- Each challenge specifies clear objectives derived directly from the tutorial implementation.
- Challenges contain **zero spoiler comments**—diagnose and complete the implementation until all assertions pass.
- Run a task using Python:
  ```bash
  python practical/hour_1/task_01_env_setup.py
  ```
- When the implementation is correct, it will print:
  ```text
  ✓ Task 01 passed!
  ```

### 3. Verify Entire Practical Suite
To run and verify all 105 practical tasks across all 7 hours:
```bash
python3 -c "
import glob, subprocess, sys
for h in range(1, 8):
    for f in sorted(glob.glob(f'practical/hour_{h}/task_*.py')):
        res = subprocess.run([sys.executable, f], capture_output=True, text=True)
        if res.returncode != 0:
            print(f'FAILED: {f}')
            sys.exit(1)
print('✓ All 105 practical tasks passed successfully!')
"
```
