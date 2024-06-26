from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

pdf_path = 'data/Diagnostic and statistical manual of mental disorders _ DSM-5 ( PDFDrive.com ).pdf'  # Ensure this path is correct
company_policies_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a file for easy access
with open('data/Diagnostic and statistical manual of mental disorders _ DSM-5 ( PDFDrive.com ).txt', 'w') as f:
    f.write(company_policies_text)