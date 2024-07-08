"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import Any


class Solution(object):
    def max_profit(self, prices: Any) -> Any:
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_profit = 0
        # min_price = float('inf')
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit

        # my code
        # if not prices:
        #     # If prices is empty, there is no profit
        #     return 0
        # n=min(prices)
        # p=prices.index(n)
        # n_p=0
        # profit=0
        # if prices[p] != prices[-1] and prices[p] !=0:
        #     n_p=max(prices[p:])
        #     profit=n_p-n
        # else:
        #     prices.pop(p)
        #     if not prices:
        #         return 0
        #     else:
        #         n=min(prices)
        #         p=prices.index(n)
        #         n_p=max(prices[p:])
        #         profit=n_p-n
        # return profit

        small = prices[0]
        big = prices[0]
        diff = 0

        for i in prices:
            if i < small:
                small = i
                big = i
            elif i > big:
                big = i
                diff = max(diff, big - small)

        return diff
