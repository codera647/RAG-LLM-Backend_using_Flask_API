from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain.schema import Document


def retrieve_doc(chunks,embeddings):
    docs = [Document(page_content=text) for text in chunks]
    vector_store = Chroma.from_documents(docs,embeddings)
    vector_store_retriever = vector_store.as_retriever(search_kwargs={"k":3})

    keyword_base_retriever = BM25Retriever.from_documents(docs)
    keyword_base_retriever.k = 3

    ensemble_retriever = EnsembleRetriever(retrievers=[vector_store_retriever,
                                                       keyword_base_retriever],
                                           weights=[0.5,0.5])
    return ensemble_retriever


