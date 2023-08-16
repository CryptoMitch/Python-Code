# Challenge: Reverse Words in a String

# Reverse the words in the string while maintaining the order of characters in each word

def reverse_words(s: str) -> str: # define function with name, add parameter of type string, return value of type string
    words = s.split() # provide delimiter that splits the string into words and store in a variable
    reversed_words = list(reversed(words)) # Reverse the order of the words, convert to a list and store in a variable
    reversed_string = ' '.join(reversed_words) # Join the reversed words back into the string
    print(reversed_string) # Print the reversed string for debugging purposes
    return reversed_string # Return the reversed string to be used in other parts of the code
    
input_string = 'Mitch Loves Code'
reversed_result = reverse_words(input_string)
print("The sentence was: ", input_string)
print('The sentence backwards is: ', reversed_result)
