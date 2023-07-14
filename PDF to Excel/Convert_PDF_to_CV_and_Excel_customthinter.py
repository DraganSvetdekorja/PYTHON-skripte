import os
import tabula
import pandas as pd
from customtkinter.file_dialogs import ask_open_filename
from customtkinter.window import Tk

# Create an instance of Tk from customtkinter
root = Tk()

# Select the PDF file using a custom file dialog
pdf_path = ask_open_filename(parent=root, title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])

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


# To convert the code to use the customtkinter library for a nicer GUI experience, you can update the code as shown below:

# In this code, the customtkinter library is imported to use its custom file dialogs and window. We create an instance of Tk from customtkinter to create the main window.

# The ask_open_filename function from customtkinter.file_dialogs is used to display a file dialog and allow the user to select the PDF file. It takes the parent parameter as root to set the main window as the parent window for the file dialog.

# The rest of the code remains the same, extracting data from the PDF using Tabula, converting it to a DataFrame, and exporting it to both a CSV and an Excel file with the same name as the selected PDF file, within the same folder.

# Please make sure you have the customtkinter library installed (pip install customtkinter) before running the updated code.
