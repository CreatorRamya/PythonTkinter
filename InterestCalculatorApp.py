import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        si = (principal * rate * time) / 100

        ci = principal * ((1 + rate / 100) ** time) - principal

        result_label.config(text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

tk.Label(root, text="Interest Calculator", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Principal Amount (₹):", bg="red").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%):", bg="red").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period (Years):", bg="red").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Calculate Interest", bg="Yellow", command=calculate_interest).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()
