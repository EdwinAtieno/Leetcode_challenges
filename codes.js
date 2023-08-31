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



