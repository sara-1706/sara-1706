import tkinter as tk
import random

# Function to handle the game logic
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        update_score("user")
    else:
        result = "You lose!"
        update_score("computer")
    
    # Display the result and choices
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    play_again_button.pack()

# Function to update scores
def update_score(winner):
    global user_score, computer_score
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")

# Function to reset the game for another round
def play_again():
    result_label.config(text="")
    play_again_button.pack_forget()

# Initialize the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.config(bg="#F0F8FF")

# Initialize scores
user_score = 0
computer_score = 0

# Instructions label
instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 14), bg="#F0F8FF")
instructions_label.pack(pady=10)

# Buttons for user choice
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), bg="#8A2BE2", fg="white", command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), bg="#8A2BE2", fg="white", command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), bg="#8A2BE2", fg="white", command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#F0F8FF")
result_label.pack(pady=10)

# Label to display scores
score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer's Score: {computer_score}", font=("Arial", 12), bg="#F0F8FF")
score_label.pack(pady=10)

# Button to play again
play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), bg="#8A2BE2", fg="white", command=play_again)

# Run the application
root.mainloop()
