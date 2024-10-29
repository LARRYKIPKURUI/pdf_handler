
import PyPDF2

def read_metadata(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = pdf_reader.metadata

    print('Metadata of the pdf file is: ')
    for key, value in metadata.items():
        print(f'{key}: {value}')

read_metadata('metadata_added.pdf')


























