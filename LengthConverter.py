import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Length Converter: Inches to Centimeters")
root.geometry("300x150")

tk.Label(root, text="Enter length in inches:").pack(pady=5)
entry_inch = tk.Entry(root)
entry_inch.pack()

convert_button = tk.Button(root, text="Convert", command=convert_to_cm, bg='Orange')
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
