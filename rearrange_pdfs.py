import PyPDF2


def rearrange_pages(input_pdf, output_pdf, page_oder):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in page_oder:
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"Rearranged pdf is saved as {output_pdf}")


# call func and reversing the oder of the pdfs
rearrange_pages('merged.pdf', 'rearranged.pdf', [2, 1, 0])
