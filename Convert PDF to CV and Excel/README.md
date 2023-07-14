


# Make sure you have the tabula-py and pandas libraries installed (pip install tabula-py pandas). This code uses the askopenfilename function from the filedialog module in tkinter to display a file dialog and allow the user to select the PDF file interactively.

# The extracted data is concatenated into a single DataFrame using pd.concat(df), assuming that df is a list of DataFrames obtained from multiple pages of the PDF. You can modify this part based on your specific requirements.

# The resulting data is then exported to a CSV file and an Excel file using df.to_csv() and df.to_excel(), respectively. The paths for the output files are specified as output.csv and output.xlsx, but you can change them to your desired paths.

# After running the code, the selected PDF file will be processed, and the extracted data will be saved as a CSV file and an Excel file in the specified output paths.

# To export the extracted data to both a CSV and Excel file with the same name as the selected PDF file, into the same folder, you can modify the code as follows:


# In this code, the os module is used to extract the file name and folder path from the selected PDF file path. The os.path.basename() function retrieves the file name, and the os.path.dirname() function retrieves the folder path.

# The output file paths for the CSV and Excel files are generated using os.path.join() to combine the folder path and the desired file name. The os.path.splitext() function splits the file name into the base name and the extension, and then the file extension is changed to .csv and .xlsx for the respective output files.

# By using these modifications, the extracted data will be exported to both a CSV and an Excel file with the same name as the selected PDF file, within the same folder.

