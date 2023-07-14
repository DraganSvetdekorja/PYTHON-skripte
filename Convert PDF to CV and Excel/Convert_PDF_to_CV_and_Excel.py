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


#To read a PDF file with Tabula in Python, export the data to both a CSV and Excel file, and allow the user to select the file from a folder, you can use the following code:


# Make sure you have the tabula-py and pandas libraries installed (pip install tabula-py pandas). This code uses the askopenfilename function from the filedialog module in tkinter to display a file dialog and allow the user to select the PDF file interactively.

# The extracted data is concatenated into a single DataFrame using pd.concat(df), assuming that df is a list of DataFrames obtained from multiple pages of the PDF. You can modify this part based on your specific requirements.

# The resulting data is then exported to a CSV file and an Excel file using df.to_csv() and df.to_excel(), respectively. The paths for the output files are specified as output.csv and output.xlsx, but you can change them to your desired paths.

# After running the code, the selected PDF file will be processed, and the extracted data will be saved as a CSV file and an Excel file in the specified output paths.

# To export the extracted data to both a CSV and Excel file with the same name as the selected PDF file, into the same folder, you can modify the code as follows:


# In this code, the os module is used to extract the file name and folder path from the selected PDF file path. The os.path.basename() function retrieves the file name, and the os.path.dirname() function retrieves the folder path.

# The output file paths for the CSV and Excel files are generated using os.path.join() to combine the folder path and the desired file name. The os.path.splitext() function splits the file name into the base name and the extension, and then the file extension is changed to .csv and .xlsx for the respective output files.

# By using these modifications, the extracted data will be exported to both a CSV and an Excel file with the same name as the selected PDF file, within the same folder.

