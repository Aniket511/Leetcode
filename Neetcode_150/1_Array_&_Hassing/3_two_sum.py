"""
1. Two Sum

Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output : [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Initialize an empty dictionary to store numbers and their indices.
        pair_idx = {}

        # Step 2: Iterate over the list `nums` with index `i` and value `num`
        for i, num in enumerate(nums):
            # Step 3: Check if the complement (target - num) exists in the dictionary.
            # If the complement is found, it means we have previously encountered
            # the number that, when added to the current number, equals the target.
            if target - num in pair_idx:
                # Return the indices of the complement and the current number
                return [i, pair_idx[target - num]]

            # Step 4: If the complement is not found, add the current number and its index to the dictionary
            pair_idx[num] = i

        # If no solution is found (though the problem guarantees one solution), return an empty list.
        return []

# Time Complexity:
# O(n), where n is the number of elements in the input list `nums`.
# We loop through `nums` once, and each dictionary operation (lookup and insertion) is O(1) on average.

# Space Complexity:
# O(n), where n is the number of unique elements in `nums`.
# The dictionary `pair_idx` stores each number and its index, which can grow to be as large as the size of `nums`.

# Test case
nums = [2, 7, 11, 15]
target = 26
solution = Solution()  # Instantiate the Solution class
print(solution.twoSum(nums, target))  # Expected output: [1, 3], because nums[1] + nums[3] = 7 + 15 = 26



