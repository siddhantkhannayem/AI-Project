from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import load_rag, generate_answer, retrieve

app = FastAPI()

# Load RAG pipeline on startup
index, chunks, model = load_rag("data/HSC26_Bangla.pdf")

class Query(BaseModel):
    question: str

@app.post("/query")
def query_rag(query: Query):
    retrieved = retrieve(query.question, index, chunks, model)
    answer = generate_answer(query.question, retrieved)
    return {"question": query.question, "answer": answer, "context": retrieved}
