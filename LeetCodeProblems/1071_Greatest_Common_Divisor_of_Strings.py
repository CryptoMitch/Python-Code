# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ""    

        elif str1 + str2 == str2 + str1:
            gcd_length = self.gcd(len1, len2) 
            return str1[:gcd_length]

    def gcd(self, a: int, b:int) -> int:
        if b == 0:
            return a 
        else:
            return self.gcd(b, a % b)
