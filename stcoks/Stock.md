# Stock Profit Maximization

This algorithm is designed to maximize profit by choosing an optimal day to buy a stock and another day in the future to sell that stock. The goal is to return the maximum profit achievable from this transaction. If it's not possible to achieve any profit, the function returns 0.

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

## Function Signature

```python
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
```

## Example

### Example 1:

```python
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2:

```python
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done, and the max profit = 0.
```

## Constraints

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104

## Implementation

This function aims to determine the maximum profit that can be achieved by buying and selling stocks. The approach is to iterate through the array of stock prices, keeping track of the minimum price encountered so far and updating the maximum profit whenever a higher selling price is found.

## Solution for StockI
## Max Profit from Stock Prices

This Python class provides a solution to the problem of maximizing profit from stock prices. The goal is to choose a single day to buy one stock and choose a different day in the future to sell that stock, maximizing the profit.

### Method

#### `maxProfit(prices: List[int]) -> int`

This method takes a list of stock prices as input and returns the maximum profit that can be achieved from a single transaction.

#### Parameters

- `prices` (List[int]): A list where `prices[i]` is the price of a given stock on the ith day.

#### Returns

- `int`: The maximum profit achievable. If no profit can be achieved, it returns 0.

### Example

```python
from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        small = prices[0]
        big = prices[0]
        diff = 0

        for i in prices:
            if i < small:
                small = i
                big = i
            elif i > big:
                big = i
                diff = max(diff, big-small)

        return diff
```

### Usage

```python
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
result1 = solution.maxProfit(prices1)
print(result1)  # Output: 5

prices2 = [7, 6, 4, 3, 1]
result2 = solution.maxProfit(prices2)
print(result2)  # Output: 0
```

This solution initializes variables to track the smallest and largest stock prices encountered during the iteration, updating the maximum difference whenever a larger profit is found. The result is the maximum profit achievable from a single transaction.

----------------------------------------------------------------------------------------------------------------------------

## Readme: StockII Profit Maximization


### Explanation

This Python class provides a solution to the problem of maximizing profit from multiple transactions in stock trading. The goal is to buy and sell stocks to maximize the total profit. The provided method, `maxProfit`, takes a list of stock prices as input and returns the maximum profit that can be achieved from multiple transactions.

### Method

#### `maxProfit(prices: List[int]) -> int`

This method takes a list of stock prices as input and returns the maximum profit achievable from multiple transactions. It follows a simple strategy: buying whenever there is a potential profit (the current day's price is higher than the previous day's) and selling immediately to lock in that profit.

#### Parameters

- `prices` (List[int]): A list where `prices[i]` is the price of a given stock on the ith day.

#### Returns

- `int`: The maximum profit achievable from multiple transactions.

### Example

```python
from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
```

### Usage

```python
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)  # Output: 7
```

This solution iterates through the stock prices, and whenever it finds a potential profit (current day's price is higher than the previous day's), it adds that profit to the total profit. The result is the maximum profit achievable from multiple transactions.