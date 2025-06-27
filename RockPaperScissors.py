import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
user_choice_label = tk.Label(root, text="", font=("Arial", 14))
comp_choice_label = tk.Label(root, text="", font=("Arial", 14))

result_label.pack(pady=20)
user_choice_label.pack()
comp_choice_label.pack()

def play(user_choice):
    comp_choice = random.choice(choices)
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    result_label.config(text=result)

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

rock_btn = tk.Button(button_frame, text="Rock", width=10, bg="Pink", command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, bg="Sky blue", command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, bg="#ac84ee", command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
