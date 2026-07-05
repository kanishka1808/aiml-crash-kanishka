# AuraHealth Nexus RAG Chatbot

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot for the fictional healthcare company **AuraHealth Nexus**.

The chatbot answers user questions only from the provided internal documents using semantic search and a Large Language Model (LLM).

---

## Features

- Load multiple text documents
- Recursive text chunking
- Sentence Transformer embeddings
- FAISS Vector Database
- Semantic Retrieval
- Groq Llama 3.3-70B Answer Generation
- Conversational Chat Interface
- Source Document Display

---

## Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- HuggingFace
- Groq API
- Llama 3.3 70B
- VS Code

---

## Folder Structure

AuraHealth_RAG/

├── synthetic_data/

├── src/

│ ├── data_loader.py

│ ├── text_splitter.py

│ ├── embedding_model.py

│ ├── vector_store.py

│ ├── retriever.py

│ └── generator.py

├── app.py

├── requirements.txt

├── .gitignore

├── README.md

└── .env

---

## Workflow

1. Load Documents
2. Split into Chunks
3. Generate Embeddings
4. Store Embeddings in FAISS
5. Retrieve Relevant Chunks
6. Generate Final Answer using Groq LLM

---

## Example Questions

- Who is the Head of the OmniHeal initiative?
- What override code must be used during the Cognitive Reset Sequence?
- What percentage of the budget is allocated to logistical support?
- What specific gas is released during Crimson lockdown?

---

## Future Improvements

- Better Retrieval Ranking
- Persistent Vector Database
- Web Interface using Streamlit
- PDF Support
- Hybrid Search
- Multi-turn Memory

---

## Author

Kanishka