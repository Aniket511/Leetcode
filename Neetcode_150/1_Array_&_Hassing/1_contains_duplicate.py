"""
217. Contains Duplicate 

Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty set to keep track of elements we've seen
        seen = set()

        # Iterate through each number in the input list `nums`
        for element in nums:
            # If the element is already in the set, it means it's a duplicate
            if element in seen:
                return True  # Return True as soon as a duplicate is found
            # If the element is not in the set, add it to the set
            seen.add(element)

        # If we finish iterating through the list without finding any duplicates,
        # it means all elements are unique, so return False
        return False

# Time Complexity:
# O(n), where n is the number of elements in the list `nums`.
# We iterate through each element once, and each set operation (checking for existence and adding) takes O(1) time on average.

# Space Complexity:
# O(n), where n is the number of unique elements in the list.
# In the worst case, when all elements are unique, the set `seen` will store all elements of `nums`.

# Test case
nums = [1, 2, 3, 4, 5]
solution = Solution()
print(solution.containsDuplicate(nums))  # Expected output: False (no duplicates)
