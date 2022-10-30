from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf_list = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf in pdf_list:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
