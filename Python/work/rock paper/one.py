import tkinter as tk
import random
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="lightblue")
choices = ["Rock", "Paper", "Scissors"]
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)
    result_label.config(text="Result: " + result)
title_label = tk.Label(root, text="Rock Paper Scissors", 
                       font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=20)
rock_button = tk.Button(root, text="Rock", width=15,
                        command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15,
                         command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15,
                            command=lambda: play("Scissors"))
scissors_button.pack(pady=5)
user_label = tk.Label(root, text="Your Choice: ", 
                      font=("Arial", 12), bg="lightblue")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer Choice: ", 
                          font=("Arial", 12), bg="lightblue")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", 
                        font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack(pady=20)
root.mainloop()