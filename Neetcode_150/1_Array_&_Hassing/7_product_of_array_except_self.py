"""
238. Product of Array Except Self

Medium

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

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Step 1: Initialize the result array `result` with 1s. This will store our final result.
        result = [1] * len(nums)
        
        # Step 2: Calculate the prefix product (product of all elements to the left of the current index).
        prefix = 1  # Initialize prefix to 1, as there's no element to the left of the first element.
        for i in range(len(nums)):
            # Set the current element in `result` to be the product of all elements to the left of index `i`
            result[i] = prefix
            # Update the prefix product by multiplying with `nums[i]` for the next iteration
            prefix *= nums[i]
        
        # Step 3: Calculate the postfix product (product of all elements to the right of the current index).
        postfix = 1  # Initialize postfix to 1, as there's no element to the right of the last element.
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current value in `result[i]` by the postfix product up to index `i+1`
            result[i] *= postfix
            # Update the postfix product by multiplying with `nums[i]` for the next iteration
            postfix *= nums[i]

        # Step 4: Return the final result array `result`, which contains the product except self for each element.
        return result

# Time Complexity:
# O(n), where n is the number of elements in `nums`. We iterate through the list twice: once for the prefix product and once for the postfix product.

# Space Complexity:
# O(n), where n is the length of `nums`, because we use an additional result array `result` to store the final output.

# Test case
nums = [1, 2, 3, 4]
solution = Solution()
answer = solution.productExceptSelf(nums)
print(answer)  # Expected output: [24, 12, 8, 6], because:
               # - 1*2*3 = 24 (product except 1)
               # - 1*3*4 = 12 (product except 2)
               # - 1*2*4 = 8 (product except 3)
               # - 1*2*3 = 6 (product except 4)
