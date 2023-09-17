# Leetcode #13 Roman Numeral to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to store Roman Integers
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0 # initialise variable to store result value
        prev_value = 0

        for symbol in reversed(s):  # Iterate from right to left
            value = roman_values[symbol]
        
            if value < prev_value:
                result -= value
            else:
                result += value
            
            prev_value = value
    
        return result    