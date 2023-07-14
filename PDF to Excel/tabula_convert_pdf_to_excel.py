import tabula

# Path to your PDF file
pdf_file = "path/to/your/pdf/file.pdf"

# Path to the output Excel file
output_file = "path/to/output/file.xlsx"

# Convert PDF to Excel
tabula.convert_into(pdf_file, output_file, output_format="xlsx")
