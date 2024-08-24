from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings



def embedding_chunks():


    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

    return embeddings