from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_faiss_index(data):
    """Creates a FAISS index for the given data."""
    embeddings = model.encode(data, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

def query_faiss(index, query, data):
    """Queries the FAISS index and returns the closest match."""
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, 1)
    return data[indices[0][0]]
