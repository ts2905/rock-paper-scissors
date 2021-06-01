# game.py

import random

#Greeting. Assign user name. Assign user's move/choice to variable
print("Rock, Paper, Scissors, Shoot!")
user_name = input("What's your name?: ")
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print("")

#print(user_choice)
print(user_name,"'s choice: ",user_choice)
print("")

#if user_choice == "rock" or "paper" or "scissors":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("(Valid input confirmed...)")
    
else:
    print("OOPS, invalid input. Please try again.")
    exit()

#Invoke random module to choose computer's move from list
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("")
print("Computer's choice: ",computer_choice)
print("")

# Homework - Added validation for who won the game
if (user_choice == computer_choice):
    print(user_name,", you TIED the computer - try again.")
    print("")
    print("THIS IS THE END OF THE GAME. FEEL FREE TO PLAY AGAIN.")    
    exit()

if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You WON,", user_name,", congratulations!!!")
    print("")
    print("THIS IS THE END OF THE GAME. FEEL FREE TO PLAY AGAIN.")    
    exit()

else:
    print("You LOST - sorry ", user_name,".")
    print("")
    print("THIS IS THE END OF THE GAME. FEEL FREE TO PLAY AGAIN.")
    exit()