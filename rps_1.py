import tkinter as tk
import random

# ---------------- Game Logic ---------------- #

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"


# ---------------- Event Handlers ---------------- #

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_choice_var.set(user_choice)
    computer_choice_var.set(computer_choice)
    result_var.set(result)


def reset_game():
    user_choice_var.set("-")
    computer_choice_var.set("-")
    result_var.set("Make your move!")


# ---------------- GUI Setup ---------------- #

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x350")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Choice Display Frame
choice_frame = tk.Frame(root)
choice_frame.pack(pady=15)

user_choice_var = tk.StringVar(value="-")
computer_choice_var = tk.StringVar(value="-")

user_label_title = tk.Label(choice_frame, text="Player", font=("Arial", 12, "bold"))
user_label_title.grid(row=0, column=0, padx=40)

computer_label_title = tk.Label(choice_frame, text="Computer", font=("Arial", 12, "bold"))
computer_label_title.grid(row=0, column=1, padx=40)

user_label = tk.Label(choice_frame, textvariable=user_choice_var, font=("Arial", 12))
user_label.grid(row=1, column=0, padx=40)

computer_label = tk.Label(choice_frame, textvariable=computer_choice_var, font=("Arial", 12))
computer_label.grid(row=1, column=1, padx=40)

# Result Display
result_var = tk.StringVar(value="Make your move!")
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_btn.pack(pady=10)

# Run App
root.mainloop()
