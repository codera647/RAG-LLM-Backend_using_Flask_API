from Document_Loder import document_loader as dl                    
import Chunker.breakpoints as brkp
import Chunker.chunker as ch
import Embedder.embedder as embd
from Retriever.retriever import retrieve_doc
from Generation.llm import generation_with_docs,generation_without_doc
import os,json



   
def get_results(message,files):
 
  if files :
    for file in files:
      if os.path.exists(file):
            file_extension = os.path.splitext(file)[1].lower()
    
            if file_extension == ".pdf":
                file_type = "PDF"
            elif file_extension == ".txt":
                file_type = "Text"
            else:
                file_type = "Unknown"

            file_info = {
                  "file_name": os.path.basename(file),
                  "absolute_path": os.path.abspath(file),
                  "file_type": file_type
              }

            document = dl.doc_load(file_info)

            sen = brkp.semantic_chunking(document)

            distances,sentences = brkp.calculate_distance(sen)

            indices_above_thresh = brkp.plot(distances,sentences)

            chunks  = ch.chunking(indices_above_thresh,sentences)

            embeddings = embd.embedding_chunks()

            ensemble_retriever = retrieve_doc(chunks,embeddings)

            return generation_with_docs(ensemble_retriever,message)
      else:
          return ("File does not exist")
    
  else:
    
    return generation_without_doc(message)
   


