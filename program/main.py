import init
import json_methods as j
import os

# main
all_data = []
for current_pdf in os.listdir(r"C:/Users/jenin/OneDrive/Documents/GitHub/Data_Chunker_Python/raw_pdfs"):
    print("\nProcessing: ", current_pdf)
    if current_pdf.lower().endswith(".pdf"):  # ensure it's a PDF
        pdf_path = os.path.join(r"C:/Users/jenin/OneDrive/Documents/GitHub/Data_Chunker_Python/raw_pdfs", current_pdf)
        processor = init.PDFProcessor(pdf_path)
        all_data.extend(processor.meta_data)  # add chunks

j.write_to_json(all_data)

