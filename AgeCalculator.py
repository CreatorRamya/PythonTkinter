import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for day, month, and year.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

title_label = tk.Label(root, text="Age Calculator App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Day:", bg="#9FDE86").grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(input_frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Month:", bg="#88FE9A" ).grid(row=1, column=0, padx=5, pady=5)
month_entry = tk.Entry(input_frame, width=5)
month_entry.grid(row=1, column=1, padx=5)

tk.Label(input_frame, text="Year of Birth:", bg="#80F39B").grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(input_frame, width=5)
year_entry.grid(row=2, column=1, padx=5)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.place(x=100, y=160)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()