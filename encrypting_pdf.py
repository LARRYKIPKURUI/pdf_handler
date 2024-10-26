# Password protecting PDFs (Encrypting pdf)

import PyPDF2


def encrypt_pdf(input_pdf, output_pdf, password):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Encrypt the PDF with the given password
    pdf_writer.encrypt(password)

    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"Encrypted PDF saved as '{output_pdf}'.")


# Running the program with hope of 0 errors

encrypt_pdf('merged.pdf', 'encrypted.pdf', 'password123')
