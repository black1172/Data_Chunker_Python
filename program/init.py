import pdf_reader as r
import tokenize_text as t
import chunk_text as c

def __init__(self, filename):
    self.name = filename
    self.text = r.read_file(self.name)
    self.tokens = t.tokenize(self.text)
    self.chunks = c.chunk(self.tokens)
