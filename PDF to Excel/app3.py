import tabula
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select the PDF file using a file dialog
Tk().withdraw()
pdf_path = askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

# Extract data from PDF using Tabula
df = tabula.read_pdf(pdf_path, pages='all')

# Convert the extracted data to a DataFrame
df = pd.concat(df)

# Export the DataFrame to a CSV file
output_csv_path = "output.csv"
df.to_csv(output_csv_path, index=False)

# Export the DataFrame to an Excel file
output_excel_path = "output.xlsx"
df.to_excel(output_excel_path, index=False)

print("Data has been exported to CSV and Excel files successfully.")
