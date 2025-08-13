import pdf_reader as r
import tokenize_text as t
import chunk_text as c
import meta_data as m

class PDFProcessor:
    def __init__(self, filename):
        self.name = filename
        self.text = self.read_pdf()
        self.tokens = self.tokenize()
        self.chunks = self.chunk()
        self.meta_data = self.add_metadata()

    def read_pdf(self):
        import pdf_reader as r
        return r.read_file(self.name)

    def tokenize(self):
        import tokenize_text as t
        return t.tokenize(self.text)

    def chunk(self):
        import chunk_text as c
        return c.chunk(self.tokens)

    def add_metadata(self):
        import meta_data as m
        return m.fill_meta_data(self.chunks, filename=self.name)

