import json
import os

def write_to_json(meta_chunks):
     # Full file path
    file_path = os.path.join("C:\VS_CODE\Data_Chunker_Python\output", "chunks.json")
    
    # Write JSON
    with open(file_path, "w", encoding="utf-8") as chunked_file:
        json.dump(meta_chunks, chunked_file, ensure_ascii=False, indent=2)
    return chunked_file