# 136 Single Number

# Given a non-empty array of integers nums, 
# every element appears twice except for one. 
# Find that single one.

# You must implement a solution with 
# a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single_num = 0 
        for num in nums:
            single_num ^= num # Apply XOR operation to find the unique number
        return single_num # Return the unique number