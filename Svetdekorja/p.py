from tkinter import *

def calculate_rolls():
    # Get dimension values
    wall_width = int(wall_width_entry.get() or wall_width_entry.placeholder)
    wall_height = int(wall_height_entry.get() or wall_height_entry.placeholder)
    roll_width = int(roll_width_entry.get() or roll_width_entry.placeholder)
    roll_length = int(roll_length_entry.get() or roll_length_entry.placeholder)

    # Get matching values
    match = match_var.get()
    matching = 0
    delay = 0
    if match == 'no':
        matching = 0
        delay = 0
    elif match == 'yes':
        matching = int(matching_entry.get() or matching_entry.placeholder)
        delay = 0
    elif match == 'yes_delay':
        matching = int(matching_entry.get() or matching_entry.placeholder)
        delay = int(delay_entry.get() or delay_entry.placeholder)

    # Get other values
    trimming = int(trimming_entry.get() or trimming_entry.placeholder)
    spare = spare_var.get()

    # Calculate lines per wall
    lines_wall = 0
    if roll_width > 0:
        lines_wall = wall_width / roll_width

    # Calculate repeating of pattern
    repeating = 0
    if (matching + delay) > 0:
        repeating = wall_height / (matching + delay)

    # Calculate tape length
    tape_length = 0
    if match == 'no':
        tape_length = wall_height + trimming
    elif match == 'yes':
        tape_length = math.ceil(repeating) * matching + trimming
    elif match == 'yes_delay':
        tape_length = math.ceil(repeating) * (matching + delay) + trimming

    # Calculate tapes per roll
    tapes_rolls = 0
    if tape_length > 0:
        tapes_rolls = roll_length / tape_length

    # Calculate required rolls
    required_rolls = 0
    if math.floor(tapes_rolls) > 0:
        required_rolls = math.ceil(math.ceil(lines_wall) / math.floor(tapes_rolls))

    # Add spare roll
    if spare == 'yes':
        required_rolls += 1

    # Set result in the equation
    required_rolls_label.configure(text=str(required_rolls))

root = Tk()
root.title("Roll Calculator")

# Open popup
kalkulator_button = Button(root, text="Open popup")
kalkulator_button.grid(row=0, column=0)

# Change roll matching type
match_var = StringVar()
match_var.set("no")
match_radio1 = Radiobutton(root, text="No", variable=match_var, value="no")
match_radio2 = Radiobutton(root, text="Yes", variable=match_var, value="yes")
match_radio3 = Radiobutton(root, text="Yes with Delay", variable=match_var, value="yes_delay")
match_radio1.grid(row=1, column=0)
match_radio2.grid(row=1, column=1)
match_radio3.grid(row=1, column=2)

# When user inputs data

#text = root.StringVar()
#text.set("This is the default text")
# textBox = tk.Entry(root,textvariable = text)

wall_width_entry = Entry(root,text = "Traven we are you")
wall_height_entry = Entry(root)
roll_width_entry = Entry(root)
roll_length_entry = Entry(root)
matching_entry = Entry(root)
delay_entry = Entry(root)
trimming_entry = Entry(root)
spare_var = StringVar()
spare_var.set("no")
spare_checkbutton = Checkbutton(root, text="Yes", variable=spare_var)
wall_width_entry.grid(row=2, column=0)
wall_height_entry.grid(row=2, column=1)
roll_width_entry.grid(row=2, column=2)
roll_length_entry.grid(row=2, column=3)
matching_entry.grid(row=3, column=0)
delay_entry.grid(row=3, column=1)
trimming_entry.grid(row=3, column=2)
spare_checkbutton.grid(row=3, column=3)

calculate_button = Button(root, text="Calculate", command=calculate_rolls)
calculate_button.grid(row=4, column=0)

required_rolls_label = Label(root, text="")
required_rolls_label.grid(row=4, column=1)

root.mainloop()
