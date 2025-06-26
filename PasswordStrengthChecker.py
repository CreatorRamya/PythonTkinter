import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif length < 6:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= length <= 10:
        result_label.config(text="Password Strength: Moderate", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")
root.resizable(False, False)

heading_label = tk.Label(root, text="Enter Your Password", bg="light yellow", font=("Arial", 14))
heading_label.pack(pady=10)

password_entry = tk.Entry(root, show='*', font=("Arial", 15), width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength, bg="light green", font=("Arial", 15))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 15))
result_label.pack(pady=5)

root.mainloop()
