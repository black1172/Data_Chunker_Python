import init
import json_methods as j

# main
test1 = init.PDFProcessor("C:/VS_CODE/Data_Chunker_Python/raw_pdfs/burnout-flyer.pdf")
j.write_to_json(test1.meta_data)