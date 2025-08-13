import datetime as dt
import generate_tags as gt

def fill_meta_data(chunks, tokens, filename, encoding, tags):

    # Retrieve tags
    tags = gt.auto_tags(tokens)

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