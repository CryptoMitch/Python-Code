import unittest
import sys
import os

# Add the 'Challenges' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Challenges.reverse_words import reverse_words

class TestReverseWords(unittest.TestCase): # Define a blueprint class that inherits a set of methods
    def test_example(self):
        self.assertEqual(reverse_words("Mitch Loves Code"),"Code Loves Mitch")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")
        
    def test_single_word(self):
        self.assertEqual(reverse_words("Code"), "Code")
    
if __name__ == '__main__':
    unittest.main()