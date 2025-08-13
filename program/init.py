import pdf_reader as r
import tokenize_text as t
import chunk_text as c
import meta_data as m

class PDFProcessor:
    def __init__(self, filename):
        self.name = filename
        self.text = r.read_file(self.name)              # PDF → text
        self.tokens = t.tokenize(self.text)             # text → tokens
        self.chunks = c.chunk(self.tokens)              # tokens → chunks
        self.meta_data = m.fill_meta_data(self.chunks, filename=self.name)  # chunks → metadata
