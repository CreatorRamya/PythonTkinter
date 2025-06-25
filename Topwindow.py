from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("main")
l = Label(root, text = "This is a root window.")

top = Toplevel()
top.geometry("280x200")
top.title("topWindow")
l2 = Label(top, text = "This is a toplevel window.")

root.mainloop()