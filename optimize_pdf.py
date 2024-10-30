
import fitz #PyMuPDF

def optimize_pdf(input_file,output_file):
    pdf_document =fitz.open(input_file)
    pdf_document.save(output_file,garbage=3,deflate=True) # garbage is for reducing redundant objects and deflate is for compressing
    print(f"The optimized PDF file is saved as {output_file}")

#call function
optimize_pdf('merged.pdf','optimized.pdf')