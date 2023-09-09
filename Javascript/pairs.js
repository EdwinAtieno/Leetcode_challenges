function maxProfit(prices) {
  // Create an array to store the maximum profit at each day.
  const profits = [];

  // Initialize the maximum profit to 0.
  profits[0] = 0;

  // Iterate through the prices array from day 2 onwards.
  for (let i = 1; i < prices.length; i++) {
    // Calculate the maximum profit that could have been made by selling the asset on day i.
    let currentProfit = prices[i] - prices[i - 1] + profits[i - 1];

    // If the current profit is less than 0, set it to 0.
    if (currentProfit < 0) {
      currentProfit = 0;
    }

    // Update the maximum profit.
    profits[i] = Math.max(currentProfit, profits[i - 1]);
  }

  // Return the last 9 digits of the maximum profit.
  return profits[profits.length - 1] % 1000000000;
}

// Test the function.
const prices = [4, 1, 2, 3];
console.log(maxProfit(prices));

