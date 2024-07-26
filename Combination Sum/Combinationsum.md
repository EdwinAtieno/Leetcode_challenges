# Combinations Sum

This algorithm generates all unique combinations of distinct integers from a given array (`candidates`) that sum up to a target integer. The same number from the candidates can be chosen an unlimited number of times. Two combinations are considered unique if the frequency of at least one of the chosen numbers is different.

## Example

### Example 1:

**Input:**
```python
candidates = [2,3,6,7]
target = 7
```

**Output:**
```python
[[2,2,3],[7]]
```

**Explanation:**
- 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
- 7 is a candidate, and 7 = 7.
These are the only two combinations.

### Example 2:

**Input:**
```python
candidates = [2,3,5]
target = 8
```

**Output:**
```python
[[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3:

**Input:**
```python
candidates = [2]
target = 1
```

**Output:**
```python
[]
```

## Constraints

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

The provided test cases ensure that the number of unique combinations that sum up to the target is less than 150 combinations for the given input.


# Combination Sum

This solution provides a Python implementation for finding all unique combinations of candidates from a given array where the chosen numbers sum up to a specified target. The solution follows the backtracking approach to explore all possible combinations.

## Method:

The core logic is encapsulated in the `combinationSum` method, which takes two parameters: `candidates` (a list of distinct integers) and `target` (the target sum). The method returns a list of lists, representing all unique combinations that sum up to the target.

## Backtracking:

The backtracking is performed by the `backtrack` helper function. This function explores the combinations by iterating through the candidates and recursively trying different possibilities. The base case is when the target becomes zero, indicating a valid combination, and it appends the current combination to the result list (`res`).

## Usage:

1. **Input:**
   - `candidates`: A list of distinct integers.
   - `target`: The target sum.

2. **Output:**
   - Returns a list of lists, where each inner list represents a unique combination of candidates that sums up to the target.

## Example:

```python
# Example Usage
solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
result = solution.combinationSum(candidates, target)
print(result)
```

**Output:**
```
[[2, 2, 3], [7]]
```

This example demonstrates finding unique combinations from the `candidates` array that sum up to the `target` (7). The result is a list containing lists of integers representing valid combinations.


