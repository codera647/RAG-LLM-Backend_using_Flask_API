from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings

def semntic_chunks(document):

        model = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
        text_splitter = SemanticChunker(model)

        docs = text_splitter.create_documents(document)
        return docs