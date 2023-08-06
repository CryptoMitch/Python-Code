# Generate a secret number for the computer to guess
# Project inspiration came from Kylie Ying. I then took the project my own direction.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    number_of_guesses = 0 # Initialize a counter to track the number of guesses
    # let the user guess while the number is not the secret number
    while guess != random_number:
        #let the user enter a number
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        
        if guess == random_number:
            print("You got it!")
        elif guess < random_number:
            print("Your guess is too low")
        elif guess > random_number:
            print("Your guess is too high")
        else:
            print("You must enter a number")
            
        number_of_guesses += 1 # Increment the number of guesses
            
    print(f"The secret number is {random_number}")
    print(f"You guessed the secret number in {number_of_guesses} guesses")
    
guess(20)     
        

