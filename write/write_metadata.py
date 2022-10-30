from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add the metadata
writer.add_metadata({
    "/Author": "Martin",
    "/Producer": "Libre Writer",
})

# Save the new PDF to a file
with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)
