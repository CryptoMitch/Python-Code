# 1304. Find N Unique Integers Sum up to Zero
# Given an integer n, return any array containing n unique integers such that they add up to 0.


class Solution:
    def sumZero(self, n: int) -> List[int]:

        any_array = []

        for num in range(1, n):
            any_array.append(num)
        any_array.append(-sum(any_array))
        return any_array

        any_array = [num for num in range(1, n)]
        any_array.append(-sum(any_array))
        return any_array