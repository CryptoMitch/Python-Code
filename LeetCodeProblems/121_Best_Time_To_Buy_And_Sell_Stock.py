
# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_day, highest_day, profit = 0, 0, 0

        for i in range(len(prices)):
            if prices[i] < prices[lowest_day]:
                lowest_day = i
            elif prices[i] - prices[lowest_day] > profit:
                highest_day = i
                profit = prices[highest_day] - prices[lowest_day]

        if highest_day > lowest_day:
            print(f"The best time to buy is day {lowest_day + 1} and sell is day {highest_day + 1} .")
            print(f"Total profit is: {profit}")
            return profit
        else:
            print("No profitable transaction.")
            return 0

# Example usage
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))

# Output given: 
# The best time to buy is day 2 and sell is day 5 .
# Total profit is: 5
# 5