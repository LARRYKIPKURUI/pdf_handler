
#Extracting images from the pdf file

import fitz  # PyMuPDF

def extract_images(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)
    for page_index in range(pdf_document.page_count):
        page = pdf_document[page_index]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"{output_dir}/image_{page_index+1}_{img_index+1}.{image_ext}"

            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)

            print(f"Saved {image_filename}")

#providing the input pdf file and the output dir where you want to save it

extract_images('merged.pdf','folder')