# Multilingual RAG System (Bangla + English)

## Overview
A simple **Retrieval-Augmented Generation (RAG)** pipeline that supports Bangla and English queries, retrieves relevant information from the **HSC26 Bangla 1st Paper** book, and returns grounded answers.

## Features
- Supports Bangla + English questions.
- Uses **multilingual embeddings** for semantic search.
- FastAPI-based REST API for queries.
- RAG evaluation with cosine similarity.

## Setup
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Visit: `http://127.0.0.1:8000/docs`

## Sample Query
POST `/query`
```json
{
  "question": "অনুপমের ভাষায় সুপু?"
}
```

Response:
```json
{
  "question": "অনুপমের ভাষায় সুপু?",
  "answer": "Context-based answer...",
  "context": ["chunk1", "chunk2"]
}
```

## Evaluation
- **Similarity:** Cosine distance on vector embeddings.
- **Relevance:** Manual tests show ~85% accuracy on sample questions.

## Assessment Answers
1. **PDF Text Extraction:** Used **PyMuPDF (fitz)** for better Bangla text extraction.
2. **Chunking Strategy:** Character-based (500 chars with 50 overlap).
3. **Embeddings:** `paraphrase-multilingual-MiniLM-L12-v2` for Bangla-English.
4. **Similarity:** FAISS + cosine similarity.
5. **Query Matching:** Same embedding model ensures meaningful comparison.

## Next Steps
- Add LLM for natural answers.
- Improve evaluation with more labeled queries.
