import json

def write_to_json(meta_chunks):
    with open("chunks.json", "w", encoding="utf-8") as chunked_file:
        json.dump(meta_chunks, chunked_file, ensure_ascii=False, indent=2)
    return chunked_file