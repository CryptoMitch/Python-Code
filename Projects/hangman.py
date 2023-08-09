# Inspired by Tutorial by Kylie Ying but changed to make it my own

import random
from words import inspirational_words
import string

# In the case a word is not valid, search for valid word from words file
def find_word(words):
    # Take in the words list and randomly choose a word
    word = random.choice(words)
    # return word with lowercase
    return word.lower()

def hangman():
        word = find_word(inspirational_words) # keep track of what a valid letter is or isnt
        word_letters = set(word) # Letters in the word in an unordered collection of unique elements
        alphabet = set(string.ascii_lowercase) # Get the 26 lowercase letters from the alphabet and create a set 
        used_letters = set() # Keep track of what the user has guessed
        body_parts = 7
    
        # Use while loop to keep guessing until they get the word    
        while len(word_letters) > 0 and body_parts > 0:    #keep guessing while word letters remaining is greater than 0    
            # Show the user the currently used letters
            print('Body parts left: ', body_parts, 'Used Letters: ' + ', '.join(used_letters))
            
            # Show the user what the current word looks like, with dashes for missing letters
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word: ', ' '.join(word_list))
            
            # Get User Input
            user_letter = input('Pick your first letter:').lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print(' ')
                    
                else:
                    body_parts = body_parts -1
                    print('Oh no, the letter ', user_letter, 'is not in the word.')
                    
            elif user_letter in used_letters:
                print(f'You have already used {user_letter}. Please pick again.')
                
            else: print('Invalid letter, please use lowercase alphabet letters.')
            
        # End condition
        if body_parts == 0:
            print(body_parts)
            print("Your man is hung, better send letters to the family.")
        else:
            print('Congratulations your man is saved with', body_parts, ' body parts left.')


hangman()
    