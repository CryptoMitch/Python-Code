# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} # Set is chosen instead of list because they provide O(1) average membership checks 
        val = []
        left, right = 0, len(s)-1   # Two Pointers
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in vowels:
                    left += 1
                if s[right] not in vowels:
                    right -= 1
        
        reversed_string = ''.join(s)
        
        
        return reversed_string

# Edge cases: 
    # what if both vowels are the same character do they still get swapped?
    # What happens if you have an asymmetrical word where there are vowels but not in the mirror position?