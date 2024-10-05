import tkinter as tk
import random

def play(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result = determine_winner(player_choice, computer_choice)
    
    result_label.config(text=f"You chose {player_choice}\nComputer chose {computer_choice}\n\n{result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")  # Set window size to 400x300 pixels

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create buttons with larger font
button_font = ('Arial', 14)
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play('rock'), font=button_font, width=10)
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play('paper'), font=button_font, width=10)
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play('scissors'), font=button_font, width=10)
scissors_button.pack(side=tk.LEFT, padx=10)

# Create label to display results with larger font
result_label = tk.Label(root, text="Choose rock, paper, or scissors", font=('Arial', 16), wraplength=380)
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()