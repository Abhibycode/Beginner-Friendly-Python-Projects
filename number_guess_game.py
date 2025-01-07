"""Importing package to get a random number"""
import random

"""Generate a random number, here we have tried it from 1-10"""
number = random.randint(1, 10)

"""Welcome users to game"""
print("Welcome to number guess game. You guess the number you win")
print("Let's begin the game")

def run_game():
    """Run loop till user guess correct number"""
    while True:
        try:
            """Take input from user"""
            guess = int(input("Please enter a number: "))

            #check if number is smaller/greater or equal
            if guess < number:
                print("Number is smaller")
            elif guess > number:
                print("Number is higher")
            else:
                print("Congratulation, You won the game!!!!")

                #Once guessed number is equal to generated number break the loop
                break
        
        except ValueError:
            #With try and expect we are restricting user for integer inpur only
            print("Invalid input, Please enter a number")
        
run_game()

"""
This game can be more intresting with added number of attempts for user.
This will increase difficulty for user and enjoyable
"""