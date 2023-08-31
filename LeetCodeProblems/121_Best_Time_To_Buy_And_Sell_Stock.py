
# 121. Best Time to Buy and Sell Stock


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_day = 0
        high_after_low_day = 0
        profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[lowest_day]:
                lowest_day = i
            elif lowest_day <= high_after_low_day:
                # prepare logic
            return profit = (high_after_low_day - lowest_day)

        return [lowest_day, high_after_low_day]
        print(f"The best time to buy is {lowest_day} day and sell is {high_after_low_day} day.")
        return print(f"Total profit is: {profit}")

# Example usage
solution = Solution()
prices = 7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))