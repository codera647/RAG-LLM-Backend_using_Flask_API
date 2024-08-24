import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def combine_sentences(sentences,buffer_size=1):
    for i in range(len(sentences)):
        combined_sentences = ''

        # add sentence before
        for j in range(i-buffer_size,i):
            if j >= 0 :
                combined_sentences += sentences[j]['sentence']+' '

        # add current sentence
        combined_sentences += sentences[i]['sentence']
        
        # add after sentence
        for j in range(i+1,i+buffer_size+1):
            if j < len(sentences):
                combined_sentences += ' '+sentences[j]['sentence']
        
        # adding another key to sentence dictionary
        sentences[i]['combined_sentences'] = combined_sentences

    return sentences


# embaddings for group of sentences
def sentence_embadding(sentences):

    model = SentenceTransformer("avsolatorio/GIST-all-MiniLM-L6-v2")
    embaddings = model.encode([x['combined_sentences'] for x in sentences])

    for i,sentence in enumerate(sentences):
        sentence['embedding'] = embaddings[i]
    
    return sentences


def semantic_chunking(text):
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, but got {type(text).__name__} instead.")
    # making chunks for single sentences
    single_sentences = re.split(r'(?<=[.?!])\s+',text)
    sentences = [{'index':i, 'sentence':x} for i,x in enumerate(single_sentences)]

    # combinig 3 sentences - one sentence before and one sentence after
    sentences = combine_sentences(sentences)

    # making embedding for each group of combined sentences
    sentences = sentence_embadding(sentences)

    return sentences


def calculate_distance(sentences):
    distances = []
    
    for i in range(len(sentences)-1):
        current_embedding = sentences[i]['embedding']
        next_embedding = sentences[i+1]['embedding']

        cosine = cosine_similarity([current_embedding],[next_embedding])[0][0]

        distance = 1-cosine

        distances.append(distance)

        sentences[i]['distance'] = distance

    return distances,sentences

def plot(distances,sen):

    breakpoint_threshold = 90

    # computing chunks that are above the breakpoint thereshold which is 90%
    breakpoint_distance_threshold = np.percentile(distances,breakpoint_threshold)
    num_of_distances_above_thresh = len([x for x in distances if x>breakpoint_distance_threshold])
    indices_above_thresh = [i for i,x in enumerate(distances) if x>breakpoint_distance_threshold]

    return indices_above_thresh

    