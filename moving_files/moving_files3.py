import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Select source folder using a file dialog
root = tk.Tk()
root.withdraw()
source_folder = filedialog.askdirectory(title="Select Source Folder")

# Select destination folder using a file dialog
destination_folder = filedialog.askdirectory(title="Select Destination Folder")

# Enter the image end pattern
end_pattern = input("Enter the image end pattern (e.g., '_1.jpg'): ")

# Get the list of files in the source folder
files = os.listdir(source_folder)

# Iterate over the files and move the images matching the end pattern
for file in files:
    if file.endswith(end_pattern):
        file_path = os.path.join(source_folder, file)
        shutil.move(file_path, destination_folder)

print("Images moved successfully.")
