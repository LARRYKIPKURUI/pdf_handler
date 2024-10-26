# Merging Multiple PDF Files

from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(pdf_list, output):
    pdf_writer = PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        for num_page in range(len(pdf_reader.pages)):  # Using len() to get the number of pages
            page = pdf_reader.pages[num_page]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


merge_pdfs(['Page1.pdf', "Page2.pdf", "Page3.pdf"], "merged.pdf")

# The merged.pdf should be the output
#merged.pdf will or should be added to our files.

