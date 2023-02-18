'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        compare = list()
        compare.append(prices[0])
        size = len(prices)
        for i in range(1, size):
            if prices[i] < compare[-1]:
                compare.append(prices[i])
            else:
                compare.append(compare[-1])
        result = list(map(lambda x, y: x - y, prices, compare))
        return max(result)
