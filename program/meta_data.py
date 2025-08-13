import datetime as dt

def fill_meta_data(chunks, filename, encoding, tags):

    # Handle empty tags
    if tags is None:
            tags = []

    # Keep track of datas date
    date_str = dt.date.today().isoformat()
    meta_chunks = []

    # Loop to all chunks and add meta data
    for i, chunk_tokens in enumerate(chunks):
        meta_chunks.append({
            "id": f"{filename}_{i}",
            "title": filename.replace("_", " ").title(),
            "source": filename,
            "tags": tags,
            "date": date_str,
            "text": encoding.decode(chunk_tokens)
        })

    return meta_chunks