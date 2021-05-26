# game.py

import random

#Greeting and assign user input to variable
print("Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

#print(user_choice)
print("USER CHOICE: ",user_choice)

#if user_choice == "rock" or "paper" or "scissors":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


#Invoke random module to choose computer's move from list
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ",computer_choice)


# Homework - Add validation for who won
# Homework - Customize the player's name


print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")