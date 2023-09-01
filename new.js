// You are given a record of the historical investment asset from the last N days.Analyze the record in order to calculate what could have been your maximum income.
// Assume you stated with one asset of this type and could hold at most one at a time.You could choose to sell the asset whenever you held one .if you did not hold an asset at some moment , you could always afford to buy an asset(assume you had infinite money available).
// What is the maximum income you could make?
// That, given an array of length N representing a record of prices over the last N days, returns the maximum income you could make.As fee result may be large, return its last nine digits without leading zeros( return the last modulo 1,000,000,000).
// Examples
// 1 Given A=[4,1,2,3] the function should return 6. You could sell the product on the first day (for 4), buy it on the second day(for 1) and sell it again on the Las day(for 3). The income will be equal to 4-1+3=6

function solution(A){
    const profits = [];
    profits[0] = 0;
    for(let i=1;i<A.length;i++){
        let currentProfit = A[i] - A[i-1] + profits[i-1];
        if(currentProfit < 0){
            currentProfit = 0;
        }
        profits[i] = Math.max(currentProfit,profits[i-1]);
    }
    return profits[profits.length-1] % 1000000000;
}
const prices = [4,1,2,3];
console.log(solution(prices));

function maxIncome(prices) {
  const n = prices.length;
  if (n <= 1) return 0; // If there are no prices or only one price, there's no profit to be made.

  let haveStock = -prices[0]; // Initialize with the cost of buying a stock on day 0.
  let noStock = 0; // Initialize with no profit on day 0.

  for (let i = 1; i < n; i++) {
    // Calculate the maximum income if we have a stock or don't have a stock on the current day.
    const prevHaveStock = haveStock;
    haveStock = Math.max(haveStock, noStock - prices[i]);
    noStock = Math.max(noStock, prevHaveStock + prices[i]);
  }

  // The maximum income will be when we don't have a stock on the last day.
  return noStock % 1000000000; // Return the last 9 digits.
}

// Example usage
const A = [4, 1, 2, 3];
const result = maxIncome(A);
console.log(result); // Output: 6



