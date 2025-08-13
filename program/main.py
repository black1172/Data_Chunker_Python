import init
import json_methods as j
import os

# main
all_data = []
for current_pdf in os.listdir(r"C:/VS_CODE/Data_Chunker_Python/raw_pdfs"):
    if current_pdf.lower().endswith(".pdf"):  # ensure it's a PDF
        pdf_path = os.path.join(r"C:/VS_CODE/Data_Chunker_Python/raw_pdfs", current_pdf)
        current_pdf = init.PDFProcessor(pdf_path)  # pass full path
        all_data.extend(current_pdf.meta_data)     # add chunks to list

j.write_to_json(all_data)
