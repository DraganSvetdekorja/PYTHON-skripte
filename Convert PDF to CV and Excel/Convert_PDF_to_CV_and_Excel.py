import os
import tabula
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select the PDF file using a file dialog
Tk().withdraw()
pdf_path = askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

# Extract the file name and folder path
file_name = os.path.basename(pdf_path)
folder_path = os.path.dirname(pdf_path)

# Extract data from PDF using Tabula
df = tabula.read_pdf(pdf_path, pages='all')

# Convert the extracted data to a DataFrame
df = pd.concat(df)

# Generate the output file paths
output_csv_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + ".csv")
output_excel_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + ".xlsx")

# Export the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

# Export the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)

print("Data has been exported to CSV and Excel files successfully.")
