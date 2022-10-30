from PyPDF2 import PdfWriter

writer = PdfWriter()
writer.add_blank_page(width=200, height=200)

with open("output.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
