# 108. Convert Sorted Array to Binary Search Tree
---

## Problem Description

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a **height-balanced** binary search tree.

---

## Examples
![btree1.jpg](btree1.jpg)
### Example 1:
**Input:**
`nums = [-10, -3, 0, 5, 9]`

**Output:**
`[0, -3, 9, -10, null, 5]`

**Explanation:**
`[0, -10, 5, null, -3, null, 9]` is also accepted.

![btree2.jpg](btree2.jpg)

---

### Example 2:
**Input:**
`nums = [1, 3]`

**Output:**
`[3, 1]`

**Explanation:**
`[1, null, 3]` and `[3, 1]` are both height-balanced BSTs.

![btree.jpg](btree.jpg)

---

## Constraints:
1. `1 <= nums.length <= 10^4`
2. `-10^4 <= nums[i] <= 10^4`
3. `nums` is sorted in a strictly increasing order.
