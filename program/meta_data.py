import datetime as dt
import generate_tags as gt

def fill_meta_data(text, chunks, filename, encoding, tags):

    # Keep track of datas date
    date_str = dt.date.today().isoformat()
    meta_chunks = []

    # Loop to all chunks and add meta data
    for i, chunk_tokens in enumerate(chunks):
        chunk_text = encoding.decode(chunk_tokens)
        chunk_tags = gt.generate_tags_from_text(chunk_text)
        meta_chunks.append({
            "id": f"{filename}_{i}",
            "title": filename.replace("_", " ").title(),
            "source": filename,
            "tags": chunk_tags,
            "date": date_str,
            "text": chunk_text
        })

    return meta_chunks