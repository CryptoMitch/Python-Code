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
# keep track of what a valid letter is or isnt
    word = find_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_lowercase) # Get the 26 lowercase letters from the alphabet and create unordered collection of unique elements
    used_letters = set() # Keep track of what the user has guessed
    
    # Get User Input
    user_letter = input('Pick your first letter:').lower()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letters in word_letters:
            word_letters.remove(user_letter)
            
    elif user_letter in used_letters:
        print(f'You have already used {user_letter}. Please pick again.')
        
    else: print('Invalid letter, please use lowercase alphabet letters.')
    
user_input = input('Guess something: ') 
print(user_input)
    
    
    