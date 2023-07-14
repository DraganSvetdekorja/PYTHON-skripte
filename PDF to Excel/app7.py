import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

def button_function():
    print("button pressed")


customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)
#button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
								 corner_radius=10, 
                                 text="CTkButton",
                                 command=button_function)

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)





# button = customtkinter.CTkButton(master=root_tk,
                                 # fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
                                 # text="CTkButton",
                                 # command=button_event)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()