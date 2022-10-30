from itertools import zip_longest

from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf_list = ["file1.pdf", "file2.pdf", "file3.pdf"]
page_list = [(0, 3), (0, 1)]
input_list = []

for pdf in pdf_list:
    input_f = open("document1.pdf", "rb")
    input_list.append(input_f)

for ind, (pdf, pages) in enumerate(zip_longest(pdf_list, page_list)):
    merger.append(position=ind + 1, fileobj=pdf, pages=pages)

with open("document-output.pdf", "wb") as output:
    merger.write(output)
    merger.close()
