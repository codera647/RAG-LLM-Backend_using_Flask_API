import subprocess

def generation_with_docs(query,context):
    prompt = f"""
    You name is EchoBot a helpful AI assistant that follows instructions extremely well.
    Use the following context to answer the user question.

    Think step by step before answering the question.You will get 100$ tip 
    if you provide correct answer.

    CONTEXT : {context}

    User question :{query}
"""
    process = subprocess.Popen(
        ['ollama', 'run', 'llama3'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt)
    if process.returncode != 0:
        raise ValueError(f"Error running LLaMA 3: {stderr.strip()}")
    return stdout.strip()

def generation_without_docs(query):
    prompt = f"""
    You name is EchoBot a helpful AI assistant that follows instructions extremely well.
    Use your knowledge to answer the user question.

    Think step by step before answering the question.

    User question: {query}
"""
    process = subprocess.Popen(
        ['ollama', 'run', 'llama3'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt)
    if process.returncode != 0:
        raise ValueError(f"Error running LLaMA 3: {stderr.strip()}")
    return stdout.strip()