import tkinter
from tkinter import filedialog
import tabula
import pandas as pd
import customtkinter 

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
window = tkinter.Tk()

window.geometry("700x500")
window.title("PDF to CSV/Excel Converter")

customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)
#button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)

button = customtkinter.CTkButton(master=window,
                                 fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
								 corner_radius=10, 
                                 text="Convert PDF to CSV/Excel",
                                 command=convert_pdf_to_csv_and_excel)

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Create a button to trigger the conversion process
# convert_button = tk.Button(
    # window,
    # text="Convert PDF to CSV/Excel",
    # command=convert_pdf_to_csv_and_excel
# )
# convert_button.pack(pady=20)

# Run the application
window.mainloop()
