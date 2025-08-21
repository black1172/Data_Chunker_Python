import json
import os

def write_to_json(meta_chunks):
    # Correct output directory and file path
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')
    output_dir = os.path.abspath(output_dir)
    file_path = os.path.join(output_dir, "chunks.json")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write JSON
    with open(file_path, "w", encoding="utf-8") as chunked_file:
        json.dump(meta_chunks, chunked_file, ensure_ascii=False, indent=2)
    return file_path