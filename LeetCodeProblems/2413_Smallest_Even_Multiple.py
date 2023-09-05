#2413_Smallest Even Multiple

# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (2 * n) // gcd(2, n)
        