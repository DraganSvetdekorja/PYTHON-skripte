from tkinter import *
from PIL import ImageTk, Image

root = Tk()

f = open("data/itemIDsList.txt")
ids = []
for line in f:
    line = line.rstrip("\n")
    ids.append(line)
f.close()

imgs = []
for i in range(10):
    imgs.append(ImageTk.PhotoImage(Image.open(f"website/images/{ids[i]}.png")))
    Label(root, image=imgs[-1], width=60, height=80).grid()

root.mainloop()