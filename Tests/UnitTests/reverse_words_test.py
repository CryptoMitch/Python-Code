import unittest
import sys
print(sys.path)
import os


print("Current directory:", os.getcwd())
print("Module search paths:", sys.path)

# Add the 'Challenges' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Challenges.reverse_words import reverse_words # Use the module names without the file extension to pull in the reverse words code

class TestReverseWords(unittest.TestCase): # Define a blueprint class that inherits a set of methods
    def test_example(self):
        self.assertEqual(reverse_words("Mitch Loves Code"),"Code Loves Mitch")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")
        
    def test_single_word(self):
        self.assertEqual(reverse_words("Code"), "Code")
        
    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("Hello  my  name  is  "), "  is  name  my  Hello")
    
    
# Create a test suite

if __name__ == '__main__':
    unittest.main()