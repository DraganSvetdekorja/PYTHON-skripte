import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

def read_data(file_path):
    # Check file extension
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    return data

def display_data():
    file_path = entry.get()
    try:
        data = read_data(file_path)
        # Clear previous data
        table.delete(*table.get_children())
        table['column'] = list(data.columns)
        table['show'] = 'headings'
        for column in table['columns']:
            table.heading(column, text=column)

        for row in data.itertuples(index=False):
            table.insert('', tk.END, values=row)

    except Exception as e:
        table.delete(*table.get_children())  # Clear previous data
        table.insert('', tk.END, values=("Error: " + str(e),))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv'), ('Excel files', '*.xls;*.xlsx')])
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_path)

def filter_data():
    filter_text = filter_entry.get().lower()
    for child in table.get_children():
        values = table.item(child)['values']
        if filter_text in str(values).lower():
            table.item(child, open=True)
        else:
            table.item(child, open=False)

# Create the main window
window = tk.Tk()
window.title("CSV/Excel Viewer")
window.geometry('800x600')  # Set the window size

# Create the file path entry
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Create the browse button
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Create the display button
display_button = tk.Button(window, text="Display Data", command=display_data)
display_button.pack(pady=10)

# Create the filter entry
filter_entry = tk.Entry(window, width=50)
filter_entry.pack(pady=10)
filter_entry.bind('<KeyRelease>', lambda event: filter_data())

# Create the table
table = ttk.Treeview(window)
table.pack(fill=tk.BOTH, expand=True)

# Create the vertical scrollbar for the table
vsb = ttk.Scrollbar(window, orient="vertical", command=table.yview)
vsb.pack(side='right', fill='y')
table.configure(yscrollcommand=vsb.set)

# Run the application
window.mainloop()
