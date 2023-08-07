# Have the computer guess a number selected by the user

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("You're guess is too low, try again.")
        elif guess > random_number:
            print("You're guess is too high, try again.")
            
    print(f'Congratulations, you guessed the number {random_number} correctly.')

def computer_guess(x):
    lower_bound = 1
    upper_bound = x
    feedback = ''
    
    while feedback != 'c':
        if lower_bound != upper_bound:
            guess = random.randint(lower_bound, upper_bound)
        else:
            guess = lower_bound
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            upper_bound = guess - 1
        elif feedback == 'l':
            lower_bound = guess + 1
    
    print(f'Congratulations, you guessed the number {guess} correctly.')
            
computer_guess(100)