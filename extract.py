
#Extract text from the PDF File

import pdfplumber

def extract_text(pdf_path, output_text_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text()+'\n'

        with open(output_text_path, 'w') as text_file: #w is for write mode
            text_file.write(full_text)
        print(f'Text extracted successfully! as {output_text_path} ')

#execute
extract_text('Page1.pdf', 'output.txt')

























