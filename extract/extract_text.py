from PyPDF2 import PdfReader

pdf = "example.pdf"
page = "1"

reader = PdfReader(pdf)
page = reader.pages[page - 1]
print(page.extract_text())
