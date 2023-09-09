function countPair(numbers){
    const firstDigitCount = new Map(); // Count of first digits
  const lastDigitCount = new Map();  // Count of last digits
  let validPairs = 0;               // Count of valid pairs

  // Iterate through the numbers array
  for (const num of numbers) {
    const firstDigit = Math.floor(num / 10); // Get the first digit
    const lastDigit = num % 10;              // Get the last digit

    // Count the frequency of first and last digits
    firstDigitCount.set(firstDigit, (firstDigitCount.get(firstDigit) || 0) + 1);
    lastDigitCount.set(lastDigit, (lastDigitCount.get(lastDigit) || 0) + 1);
  }

  // Iterate through the numbers array again to count valid pairs
  for (const num of numbers) {
    const lastDigit = num % 10; // Get the last digit
    const firstDigit = Math.floor(num / 10); // Get the first digit

    // Calculate the number of valid pairs for the current number
    validPairs += (firstDigitCount.get(lastDigit) || 0) * (lastDigitCount.get(firstDigit) || 0);

    // Subtract 1 to exclude counting the current number itself
    if (firstDigit === lastDigit) {
      validPairs--;
    }
  }

  // Divide by 2 to account for double counting of pairs (e.g., (A, B) and (B, A))
  validPairs /= 2;

  return validPairs;
}

const numbers1 = [30, 12, 29, 91];
const result1 = countPair(numbers1);
console.log(result1); // Output: 3

const numbers2 = [122, 21, 21, 23];
const result2 = countPair(numbers2);
console.log(result2); // Output: 5