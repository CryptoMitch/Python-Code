#You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

class Solution:
    def mergeAlternately(self, word1, word2) -> str:

        s1, s2 = 0, 0
        merged_string = ''

        # Main code goes here
        while s1 < len(word1) or s2 < len(word2):
            if s1 < len(word1):
                merged_string += word1[s1]
            if s2 < len(word2):
                merged_string += word2[s2]
            s1 += 1
            s2 += 1
        
        return merged_string
    
    # Code I tried that didn't work
       # merged_string = merged_string.join([word1[0]], [word2[0]], [word1[1]], [word2[1]], [word1[2]], [word2[2]])