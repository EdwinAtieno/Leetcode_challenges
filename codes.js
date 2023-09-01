function room(A) {
    // Sort the array A in descending order based on the maximum number of guests allowed
    A.sort((a, b) => b - a);

    // Initialize variables to keep track of the minimum number of rooms needed
    let minRooms = 1;
    let currGuests = 0;

    // Loop through the sorted array and assign guests to rooms
    for (let k = 0; k < A.length; k++) {
        // Get the maximum number of guests allowed for the current guest
        let maxGuests = A[k];

        // If there are already enough guests in the current room, start a new room
        if (currGuests >= maxGuests) {
            minRooms++;
            currGuests = 0;
        }

        // Add the current guest to the current room
        currGuests++;
    }

    // Return the minimum number of rooms needed
    return minRooms;
}

// Example usage
const A = [7, 3, 1, 1, 4, 5, 4, 9];
console.log(room(A));



function solution(A){
    A.sort((a,b)=>b-a);
    let minRooms = 1;
    let currGuests = 0;
    for(let i=0;i<A.length;i++){
        let maxGuests = A[i];
        if(currGuests >= maxGuests){
            minRooms++;
            currGuests = 0;
        }
        currGuests++;
    }
    return minRooms;
}

//there is an array number made of N integers. each number has at least two digits and its first and last digits are different. you can selsect a pair of numbers if the last digit of the first selected number is the same as the first digit  of the second number. calculate the number of ways in which such a pair of numbers can be selected. example numbers = [30,12,29,91] the function should return 3. the pairs are: (12,29), (29,91),(91,12)
function Solutions(numbers) {
  let count = 0;
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i].toString().charAt(numbers[i].toString().length - 1) === numbers[j].toString().charAt(0)) {
        count++;
      }
    }
  }
  return count;
}
//

function countValidPairs(numbers) {
  const firstDigitMap = new Map(); // Map to store numbers with the same first digit
  const lastDigitMap = new Map();  // Map to store numbers with the same last digit

  let count = 0; // Initialize the count of valid pairs

  // Iterate through the numbers array
  for (const num of numbers) {
    const firstDigit = Math.floor(num / 10); // Extract the first digit
    const lastDigit = num % 10;              // Extract the last digit

    // Count pairs with the same last digit as the current number's first digit
    if (firstDigitMap.has(lastDigit)) {
      count += firstDigitMap.get(lastDigit);
    }

    // Update the maps to store the current number
    firstDigitMap.set(firstDigit, (firstDigitMap.get(firstDigit) || 0) + 1);
    lastDigitMap.set(lastDigit, (lastDigitMap.get(lastDigit) || 0) + 1);
  }

  return count;
}

// Example usage
const numbers = [30, 12, 29, 91];
const result = countValidPairs(numbers);
console.log(result);

function findPairs(numbers) {
  // Create an empty set to store the pairs of numbers found.
  const pairs = new Set();

  // Iterate through the array of numbers.
  for (let i = 0; i < numbers.length; i++) {
    // Iterate through the remaining numbers in the array.
    for (let j = i + 1; j < numbers.length; j++) {
      // If the last digit of the current number is the same as the first digit of the next number,
      // then the two numbers are added to the set `pairs`.
      if (numbers[i].slice(-1) === numbers[j].slice(0, 1)) {
        pairs.add([numbers[i], numbers[j]]);
      }
    }
  }

  // Return the length of the set `pairs`.
  return pairs.size;
}

function countPairs(numbers) {
   const pairs = new Set();

  // Iterate through the array of numbers.
  for (let i = 0; i < numbers.length; i++) {
    // Iterate through the remaining numbers in the array.
    for (let j = i + 1; j < numbers.length; j++) {
      // Get the last digit of the first number and the first digit of the second number.
      const lastDigit1 = numbers[i] % 10;
      const firstDigit2 = numbers[j] / 10;

      // If the last digit of the first number is the same as the first digit of the second number,
      // then the two numbers are added to the set `pairs`.
      if (lastDigit1 === firstDigit2) {
        pairs.add([numbers[i], numbers[j]]);
      }
    }
  }

  // Return the length of the set `pairs`.
  return pairs.size;

}
const numberas = [30, 12, 29, 91];


console.log(countPairs(numberas));