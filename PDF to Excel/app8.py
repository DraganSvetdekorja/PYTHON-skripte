import tkinter as tk
from tkinter import filedialog
import tabula
import pandas as pd
import customtkinter as ctk


def convert_pdf_to_csv_and_excel():
    # Select PDF files to convert
    file_paths = filedialog.askopenfilenames(
        title='Select PDF Files',
        filetypes=[('PDF Files', '*.pdf')]
    )

    for file_path in file_paths:
        # Extract file name and folder path
        folder_path, file_name = file_path.rsplit('/', 1)
        file_name = file_name.split('.')[0]

        # Convert PDF to CSV
        csv_path = f"{folder_path}/{file_name}.csv"
        tabula.convert_into(file_path, csv_path, output_format='csv', pages='all')

        # Convert CSV to Excel
        excel_path = f"{folder_path}/{file_name}.xlsx"
        df = pd.read_csv(csv_path)
        df.to_excel(excel_path, index=False)

    print("Conversion completed successfully.")


# Create the main window
window = ctk.ThemedTk()
window.set_theme("dark")  # Set the dark theme

window.title("PDF to CSV/Excel Converter")

# Create a button to trigger the conversion process
convert_button = ctk.ThemedButton(
    window,
    text="Convert PDF to CSV/Excel",
    command=convert_pdf_to_csv_and_excel
)
convert_button.pack(pady=20)

# Run the application
window.mainloop()
