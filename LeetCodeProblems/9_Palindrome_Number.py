# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reversed_x = 0

        if x == 0:
            return True

        # Check if negative
        elif x < 0 or (x % 10 == 0):
            return False
        
        # Check if Palindrome
        while x > 0:
            reversed_x = (reversed_x * 10) + (x % 10)
            x = x // 10
        return number == reversed_x
