from tkinter import*

window = Tk()
window.title("Sample frame")
window.geometry("400x300")

border_effects = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

for r in border_effects:
    frame = Frame(master=window, relief=r, borderwidth=5)
    frame.pack(side=LEFT)
    label = Label(master=frame, text=r)
    label.pack()
    
f1 = Frame(master=window)
f1.pack()

btn = Button(master=f1, text="click here", fg="blue")
btn.pack()

f2 = Frame(master=window, bg= "pink", height=150, width=250)
f2.pack()
window.mainloop()