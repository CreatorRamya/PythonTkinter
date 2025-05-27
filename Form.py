from tkinter import *
from datetime import date 

root = Tk()
root.title('Adding Widgets')
root.geometry('500x400')

lbl = Label(text = "Hello there!!", fg="white", bg="#ffaff3", height=1, width=400 )

name_lbl = Label(text="Full name", bg="#f74ede")
name_entry = Entry()

def display() :
    name = name_entry.get()
    global message
    message = "Welcome to the application! \nToday's date: "
    greet = "Hello "+name+" \n "

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=5)

btn = Button(text="Begin", command=display, height=3, bg="#6f1462", fg="white" )

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root = Tk()