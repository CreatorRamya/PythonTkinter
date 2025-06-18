from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    messagebox.showwarning("Warning!", "A virus is detected!")

def msg2():
    messagebox.askyesno("Quick Question!", "Did you download an unsafe file?")

#button = Button(root, text="Scan to check", command=msg)
#button.place(x=200, y=200)
button = Button(root, text="Click here", command=msg2)
button.place(x=250, y=250)

root.mainloop()