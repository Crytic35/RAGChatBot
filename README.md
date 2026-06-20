# RAGChatBot

A Retrieval-Augmented Generation (RAG) chatbot built using LangChain, ChromaDB, HuggingFace embeddings, and Google Gemini (LLM). The system retrieves relevant information from the external knowledge sources and uses it to generate accurate and context-aware responses.

---

## Overview

LLMs are powerful but limited by their static training data. RAG overcomes this limitation by combining information retrieval with language generation. Instead of relying entirely on internal model knowledge, the system retrieves relevant information from a knowledge base and provides it to the model during inference.

---

## Architecture

```
 Knowledge Sources
         ↓
  Document Loader
         ↓
   Text Splitter
         ↓
  Embedding Model
         ↓
  Vector Database
         ↓
     Retriever
         ↓
Large Language Model
         ↓
 Generated Response
```

---

## Components

### Document Loader
Loads external documents and converts them into a format suitable for processing.

### Text Splitter
Divides large documents into smaller chunks while preserving contextual information.

### Embedding Model
Transforms text into numerical vector representations that capture semantic meaning.

### Vector Database
Stores embeddings and metadata to enable efficient semantic similarity search.

### Retriever
Identifies and retrieves the most relevant information corresponding to a user query.

### Large Language Model
Generates responses using both the user query and the retrieved context.

---

## Technologies Used

- **LangChain**
- **ChromaDB**
- **HuggingFace Embeddings**
- **Google Gemini 2.5 Flash (since it has free API and LangChain support)**
- **Python**

---

## Future Improvements

- Integration with GitHub for repository monitoring and code assistance.
- Support for external APIs and real-time information sources.
- Hybrid search mechanisms.
- Long-term memory and conversation persistence.
- Autonomous and agentic workflows using LangGraph.
- Multi-agent collaboration for complex tasks and decision making.
- Integration with the Model Context Protocol (MCP) for standardized tool access.

---

## References

- LangChain Documentation: https://docs.langchain.com/
- ChromaDB Documentation: https://docs.trychroma.com/
- Hugging Face Sentence Transformers: https://www.sbert.net/
- Google Gemini API Documentation: https://ai.google.dev/

---