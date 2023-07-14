import openpyxl
from openpyxl import load_workbook
from googletrans import Translator
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select the Excel file using a file dialog
Tk().withdraw()
file_path = askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

# Load the Excel file
workbook = load_workbook(filename=file_path)
sheet = workbook.active

# Select the column to translate
column_number = input("Enter the column number (e.g., A, B, C): ")
column = sheet[column_number]

# Initialize the translator
translator = Translator()

# Translate the column values
for cell in column:
    # Detect the language of the cell value
    detection = translator.detect(cell.value)
    detected_language = detection.lang

    # Translate the cell value to Slovene
    translation = translator.translate(cell.value, src=detected_language, dest='sl')
    translated_text = translation.text

    # Print the translated text
    print(f"Original: {cell.value} | Detected Language: {detected_language} | Translated: {translated_text}")

# Save the changes to the Excel file
workbook.save(file_path)
