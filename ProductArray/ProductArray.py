"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 1. get the product of all the elements in the array
    # 2. divide the product by the element at index i
    # 3. append the result to a new array
    # 4. return the new array

    product = 1
    for num in nums:
        product *= num

    result = []
    for num in nums:
        result.append(product / num)

    return result

def productExceptSelfs(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 1. get the product of all the elements in the array
    # 2. divide the product by the element at index i
    # 3. append the result to a new array
    # 4. return the new array

    n = len(nums)
    prefix = 1
    postfix = 1
    output = [1] * n
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    return output


print(productExceptSelf([1,2,3,4]))