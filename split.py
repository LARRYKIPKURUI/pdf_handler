import os

#Splitting pdf file to multiple PDF files/pages

import PyPDF2
from PyPDF2 import PdfWriter, PdfReader


def split_pdf(pdf_path, output_dir):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = f"{output_dir}/page_{page_num + 1}.pdf"

        with open(output_path, "wb") as out:
            pdf_writer.write(out)
            print(f"Page {page_num + 1} written to {output_path}")

#Call the func
split_pdf('merged.pdf','pdf_files')

























