import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def resize_images_in_folder(folder_path, target_width):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Construct the full file path
            file_path = os.path.join(root, file_name)

            # Check if the file is an image
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                try:
                    # Open the image file
                    image = Image.open(file_path)

                    # Calculate the new height while maintaining proportions
                    width, height = image.size
                    new_height = int(target_width * height / width)

                    # Resize the image
                    resized_image = image.resize((target_width, new_height))

                    # Save the resized image, overwriting the original file
                    resized_image.save(file_path)

                    print(f"Resized '{file_name}' successfully.")
                except Exception as e:
                    print(f"Error resizing '{file_name}': {str(e)}")

def select_folder():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a folder
    folder_path = filedialog.askdirectory()

    # Check if a folder was selected
    if folder_path:
        # Resize images in the selected folder and subfolders
        resize_images_in_folder(folder_path, 1000)
    else:
        print("No folder selected.")

# Prompt the user to select a folder and resize images in the folder and subfolders
select_folder()
