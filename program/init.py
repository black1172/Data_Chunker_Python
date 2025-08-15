class PDFProcessor:
    def read_pdf(self):
        import fitz  # PyMuPDF
        import pytesseract
        from PIL import Image
        import io

        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

        pdf_doc = fitz.open(self.name)
        all_text = ""

        for page_num in range(len(pdf_doc)):
            page = pdf_doc[page_num]
            text = page.get_text().strip()

            print("\nProcessing page: ", page_num + 1)

            if text:  
                # Text was found normally, no OCR needed
                all_text += text + "\n"
            else:
                # No text found → run OCR on the rendered image
                pix = page.get_pixmap(dpi=300)  
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                ocr_text = pytesseract.image_to_string(img)
                all_text += ocr_text + "\n"

        pdf_doc.close()
        return all_text

    def tokenize(self):
        import tokenize_text as t
        return t.tokenize(self.text)

    def chunk(self):
        import chunk_text as c
        return c.chunk(self.tokens)

    def add_metadata(self):
        import meta_data as m
        import tiktoken as tt
        return m.fill_meta_data(
            self.text,
            self.chunks,
            filename=self.name,
            encoding=tt.get_encoding("cl100k_base"),
            tags=["RA"]
        )

    def __init__(self, filename):
        self.name = filename
        self.text = self.read_pdf()
        self.tokens = self.tokenize()
        self.chunks = self.chunk()
        self.meta_data = self.add_metadata()
