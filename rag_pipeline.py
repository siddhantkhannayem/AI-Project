import faiss
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from preprocess import extract_and_clean_text

def create_chunks(text, chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

def create_vector_store(chunks, model):
    vectors = model.encode(chunks, convert_to_numpy=True)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index

def retrieve(query, index, chunks, model, top_k=3):
    q_vec = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_vec, top_k)
    return [chunks[i] for i in indices[0]]

def generate_answer(query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)
    return f"Context-based answer:\n{context}"

def load_rag(pdf_path):
    text = extract_and_clean_text(pdf_path)
    chunks = create_chunks(text)
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    index = create_vector_store(chunks, model)
    return index, chunks, model
