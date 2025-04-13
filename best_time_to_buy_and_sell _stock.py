
from typing import List
"""
121. Best Time to Buy and Sell Stock (LeetCode)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # left = buy, right = sell
        maxProfit = 0

        while right < len(prices):
            #profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: # if loss made
                left = right
            right +=1

        return maxProfit



