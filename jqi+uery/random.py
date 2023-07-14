import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
window = tk.Tk()
window.title("My Tkinter Application")
window.geometry("500x500")


# Create a button
button = tk.Button(window, text="Click me", command=button_click)
button.pack()

# Run the main event loop
window.mainloop()
