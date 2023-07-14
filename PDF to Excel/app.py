import os
import tabula
import tkinter as tk
from tkinter import filedialog

def convert_pdf_to_excel(pdf_path, output_export_path):
	df = tabula.read.pdf(input_path=pdf_path, pages="all")
	tabula.convert_into(input_path=pdf_path, output_path=output_export_path, output_format="xlsx", pages='all', stream=True)

def select_folder():
    folder_path = filedialog.askdirectory()
    convert_button.config(state="normal")
    folder_path_label.config(text="Selected Folder: " + folder_path)

def convert_files():
    selected_folder = folder_path_label.cget("text").replace("Selected Folder: ", "")
    for filename in os.listdir(selected_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(selected_folder, filename)
            output_path = os.path.splitext(pdf_path)[0] + ".xlsx"
            convert_pdf_to_excel(pdf_path, output_path)
            conversion_status.config(text="Conversion completed.")

# Create the GUI
root = tk.Tk()
root.title("PDF to Excel Converter")
root.geometry("500x200")


select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=10)

folder_path_label = tk.Label(root, text="Selected Folder: ")
folder_path_label.pack()

convert_button = tk.Button(root, text="Convert to Excel", bg='#ffffff', activebackground='#00ff00', command=convert_files, state="disabled")
convert_button.pack(pady=10)

conversion_status = tk.Label(root, text="")
conversion_status.pack()

root.mainloop()
