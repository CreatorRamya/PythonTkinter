from tkinter import*

root = Tk()
root.title('Number pad')
root.geometry('300x350')

frame = Frame(master=root, height=400, width=560, bg="#af1c99")
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*'] ]

for i in range(4):

    root.columnconfigure(i, weight=1, minsize=80)
    root.rowconfigure(i, weight=1, minsize=55)

    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=2
        )
        frame.grid(row=i, column=j)

        label = Label(master=frame, text=nums[i][j], bg="#1cabaf")
        label.pack(padx=3, pady=3)

root.mainloop()