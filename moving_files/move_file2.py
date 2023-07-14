import tkinter as tk
from tkinter import filedialog
import os
import shutil

# Create a tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user to select the source folder using the file explorer
source_folder = filedialog.askdirectory(title="Select Source Folder")

# Ask the user to select the destination folder using the file explorer
destination_folder = filedialog.askdirectory(title="Select Destination Folder")

# Function to move images based on their file name endings
def move_images(source, destination, ending):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination, exist_ok=True)

    # Get a list of all files in the source folder
    files = os.listdir(source)

    for file in files:
        if file.endswith(ending):
            source_path = os.path.join(source, file)
            destination_path = os.path.join(destination, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination}")

# Prompt the user to enter the file name ending they want to move
ending = input("Enter the file name ending you want to move (e.g., '_1.jpg'): ")

# Call the move_images function with the provided inputs
move_images(source_folder, destination_folder, ending)
