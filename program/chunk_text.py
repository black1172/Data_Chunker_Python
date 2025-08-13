def chunk(tokens, chunk_size=150, overlap=15):

    # Declarations
    chunks = []
    start_index = 0

    # Chunking Loop
    while start_index < len(tokens):
        end_index = start_index + chunk_size
        chunk_tokens = tokens[start_index:end_index]
        chunks.append(chunk_tokens)
        start_index += chunk_size - overlap  # move forward, keep overlap

    return chunks