# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) # calculate the length of the input list

        # Outer Loop
        for i in range(n): # iterate through each index of the list
            current_number = target - nums[i] # calculate value needed to achieve target sum
            
            # Inner Loop
            for j in range(i+1, n): # find a number that gives target value when added
                if current_number == nums[j]: # check to see if that number is in the list

                    return [i,j] # if true return the indices of the two elements

