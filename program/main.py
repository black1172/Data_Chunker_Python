import init
import json_methods as j

# main
test1 = init.PDFProcessor("raw_pdfs\test1.pdf")
j.write_to_json(test1.meta_data)