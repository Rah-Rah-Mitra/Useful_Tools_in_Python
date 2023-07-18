from PyPDF2 import PdfReader, PdfWriter

# Define the input file path
input_file = "Art of Electronics 2020 (Paul Horowitz, Winfield Hill) (Z-Library).pdf"

# Define the output file path
output_file = "modified_file.pdf"

# Define the start page (inclusive deletion)
start_page = 1226

# Open the PDF file
pdf = PdfReader(input_file)

# Create a new PDF writer
output_pdf = PdfWriter()

# Iterate through the pages and add them to the output PDF
for page_number in range(len(pdf.pages)):
    if page_number < start_page-1:
        page = pdf.pages[page_number]
        output_pdf.add_page(page)

# Save the modified PDF to a new file
with open(output_file, "wb") as f:
    output_pdf.write(f)

print("Pages deleted successfully. Modified PDF saved as", output_file)
