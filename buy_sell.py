'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      profit = 0
      i = len(prices) - 1
      while i > 0:
        while i > 0 and prices[i] <= prices[i - 1]: 
          i -= 1
        sell = prices[i]
        while i > 0 and prices[i] >= prices[i - 1]:
          i -= 1
        buy = prices[i]
        profit += (sell - buy)
      return(profit)
