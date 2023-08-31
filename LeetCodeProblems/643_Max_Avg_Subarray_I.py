# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        array_length = len(nums)
        subarray_sum = sum(nums[:k]) # Select first k elements
        max_sum = subarray_sum # Assign the max sum to answer

        # Sliding window problem logic

        for i in range(k, array_length):
            current_window = subarray_sum + nums[i] - nums[i - k] # sum integers
            # store max number in max
            max_sum = max(max_sum, current_window)
            subarray_sum = current_window

        return max_sum / k
