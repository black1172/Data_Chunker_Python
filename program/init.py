class PDFProcessor:
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
        import tiktoken as tt
        return m.fill_meta_data(self.text, self.chunks, filename=self.name, encoding = tt.get_encoding("cl100k_base"), tags = ["RA"])
    
    def __init__(self, filename):
        self.name = filename
        self.text = self.read_pdf()
        self.tokens = self.tokenize()
        self.chunks = self.chunk()
        self.meta_data = self.add_metadata()

