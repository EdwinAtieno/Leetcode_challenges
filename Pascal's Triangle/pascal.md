# Pascal's Triangle

## Problem Statement

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

## Examples

### Example 1:

**Input:**
```plaintext
numRows = 5
```

**Output:**
```plaintext
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

**Debugging Logs:**
```plaintext
Input numRows: 5
Row 1: [1]
Row 2: [1, 1]
Row 3: [1, 2, 1]
Row 4: [1, 3, 3, 1]
Row 5: [1, 4, 6, 4, 1]
```

### Example 2:

**Input:**
```plaintext
numRows = 1
```

**Output:**
```plaintext
[[1]]
```

**Debugging Logs:**
```plaintext
Input numRows: 1
Row 1: [1]
```

## Constraints
- `1 <= numRows <= 30`
- `1 <= numRows[i][j] <= 100`