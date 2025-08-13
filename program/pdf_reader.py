import fitz

# Translate pdf to readable text
def read_file(file_name):
    text = ""
    document = fitz.open(file_name)
    for page in document:
        text += page.get_text("text")
    document.close()
    return text




