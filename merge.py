# Merging Multiple PDF Files

from PyPDF2 import PdfReader, PdfWriter
import os


def merge_pdfs(input_folder, output_pdf):
    # remove existing merge.pdf if existing
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Get a list of pdfs in the input dir
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]

    # sort
    pdf_files.sort()

    # create

    pdf_writer = PdfWriter()
    # loop through each pdf file and merge
    for pdf in pdf_files:
        with open(os.path.join(input_folder, pdf), "rb") as file:
            pdf_reader = PdfReader(file)
            for num_page in range(len(pdf_reader.pages)):  # Using len() to get the number of pages
                page = pdf_reader.pages[num_page]
            pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
    # print(f'Merged pdf saved as {output_pdf}')


input_folder = 'pdf_files'
output_folder = 'pdf_files/merged.pdf'
# merge_pdfs('input_folder', 'output_pdf')

# The merged.pdf should be the output
# merged.pdf will or should be added to our files.

#create executable exe
#pip install auto-py-to-exe
#python -m auto_py_to_exe...........to run it