# Have the computer guess a number selected by the user

import random

User_number = input("Pick any number: ")






def computer_guess(x):
    lower_bound = 1
    upper_bound = x
    feedback = ''
    
    while feedback == 'a':
        guess = random.randint(lower_bound, upper_bound)
        