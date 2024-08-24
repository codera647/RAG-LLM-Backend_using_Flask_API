from langchain_community.llms import HuggingFaceHub
from Generation.api_token import huggingfacehub_api as api
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = HuggingFaceHub(
        # repo_id = "HuggingFaceH4/zephyr-7b-beta",
        # repo_id = "mistralai/Mistral-7B-Instruct-v0.3",
        repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1",
        model_kwargs = {"temperature":0.4,"max_new_tokens":1000},
        huggingfacehub_api_token = api
    )

def extract_answer(llm_output):
 
    if "<|assistant|>" in llm_output:
        return llm_output.split("<|assistant|>")[-1].strip()
    return llm_output.strip()

def generation_with_docs(ensemble_retriever,query):


    template = """
    <|system|>
    You name is EchoBot a helpful AI assistant that follows instructions extremely well.
    Use the following context to answer the user question.

    Think step by step before answering the question.You will get 100$ tip 
    if you provide correct answer.

    CONTEXT : {context}
    </s>

    <|user|>
    {query}
    
    </s>
    <|assistant|>
"""
    
    prompt = ChatPromptTemplate.from_template(template)
    OutputParser = StrOutputParser()

    chain = (
        {"context":ensemble_retriever,"query":RunnablePassthrough()}
        | prompt
        | llm
        | OutputParser
    )

    response =  chain.invoke(query)
    answer = extract_answer(response)
    return answer

def generation_without_doc(query):

    template = """
    <|system|>
    You name is EchoBot a helpful AI assistant that follows instructions extremely well.
    Use your knowledge to answer the user question.

    Think step by step before answering the question.
    </s>

    <|user|>
    {query}

    </s>
    <|assistant|>
"""
    prompt = ChatPromptTemplate.from_template(template)
    OutputParser = StrOutputParser()  

    chain = (
        {"query":RunnablePassthrough()}
        | prompt
        | llm
        | OutputParser
    )

    response = chain.invoke(query)
    answer = extract_answer(response)
    return answer