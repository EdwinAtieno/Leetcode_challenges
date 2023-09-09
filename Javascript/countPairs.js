//You are given a record of the historical investment asset from the last N days.Analyze the record in order to calculate what could have been your maximum income.
// Assume you stated with one asset of this type and could hold at most one at a time.You could choose to sell the asset whenever you held one .if you did not hold an asset at some moment , you could always afford to buy an asset(assume you had infinite money available).
// What is the maximum income you could make?
// That, given an array of length N representing a record of prices over the last N days, returns the maximum income you could make.As fee result may be large, return its last nine digits without leading zeros( return the last modulo 1,000,000,000).
// Examples
//
function solution(A){
  let maxIncome =0;
  let current = A

}

function maxIncome(prices) {
  if (!prices.length) {
    return 0;
  }

  let maxProfit = 0;
  let minPrice = prices[0];

  for (let price of prices) {
    minPrice = Math.min(minPrice, price);
    maxProfit = Math.max(maxProfit, price - minPrice);
  }

  return maxProfit;
}

// Example
const prices = [4, 1, 2, 3];
const result = maxIncome(prices);
console.log(result % 1000000000); // Print the last nine digits

function countPairsWithMatchingDigits(numbers) {
  const digitPairs = {};
  let count = 0;

  for (let num of numbers) {
    const firstDigit = String(num)[0];
    const lastDigit = String(num)[String(num).length - 1];

    if (digitPairs[lastDigit + firstDigit]) {
      count += digitPairs[lastDigit + firstDigit];
    }

    if (digitPairs[firstDigit + lastDigit]) {
      digitPairs[firstDigit + lastDigit]++;
    } else {
      digitPairs[firstDigit + lastDigit] = 1;
    }
  }

  return count;
}

// Example
const numbers = [30, 12, 29, 91];
const result = countPairsWithMatchingDigits(numbers);
console.log(result);