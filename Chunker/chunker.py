
def chunking(indices_above_thresh,sentences):

    start_index = 0
    chunks = []

    for index in indices_above_thresh:

        group = sentences[start_index : index]
        combined_text = ' '.join([d['sentence'] for d in group])
        chunks.append(combined_text)

        start_index = index

    if start_index < len(sentences):
        combined_text = ' '.join([d['sentence'] for d in sentences[start_index:]])
        chunks.append(combined_text)        
    
    return chunks


