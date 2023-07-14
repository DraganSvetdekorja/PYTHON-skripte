from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

# Perform an action when the button is clicked
def button_click():
    inputValue = input_entry.get()
    messagebox.showinfo('Result', 'You entered: ' + inputValue)

# Simulating the document ready event
root = Tk()
root.title('Example')
root.geometry('300x100')

# Create an input field
input_entry = Entry(root)
input_entry.pack()

# Create a button and associate the button_click function
button = Button(root, text='Click Me', command=button_click)
button.pack()

root.mainloop()
