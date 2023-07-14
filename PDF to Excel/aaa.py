import tkinter as tk
from tkinter import filedialog
import tabula

def select_pdf_file():
    filetypes = [('PDF Files', '*.pdf')]
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        convert_to_excel(file_path)

def convert_to_excel(pdf_file):
    output_file = pdf_file[:-4] + '.xlsx'  # Output Excel file path
    tabula.convert_into(pdf_file, output_file, output_format='xlsx', pages='all')
    print('Conversion complete!')

# Create the main Tkinter window
window = tk.Tk()
window.title('PDF to Excel Converter')

# Create the select file button
select_button = tk.Button(window, text='Select PDF File', command=select_pdf_file)
select_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
