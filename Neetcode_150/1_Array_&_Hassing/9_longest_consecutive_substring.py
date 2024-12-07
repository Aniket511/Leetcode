"""
128. Longest Consecutive Sequence

Medium

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Step 1: Convert the list to a set for O(1) lookups
        numset = set(nums)
        longest_sequence = 0  # Variable to keep track of the longest sequence

        # Step 2: Iterate through each number in the list
        for number in nums:
            # Step 3: Check if the number is the start of a new sequence
            if number - 1 not in numset:
                current_sequence = 1  # Start with the current number as the beginning of the sequence

                # Step 4: Continue counting the sequence as long as consecutive numbers exist
                while number + current_sequence in numset:
                    current_sequence += 1

                # Step 5: Update the longest sequence found so far
                longest_sequence = max(longest_sequence, current_sequence)

        # Step 6: Return the length of the longest consecutive sequence
        return longest_sequence


# Time Complexity:
# O(n), where n is the number of elements in `nums`. We loop through the list once, 
# and for each number, we check for consecutive numbers in the set, which takes O(1) time.

# Space Complexity:
# O(n), where n is the number of elements in `nums`. We use a set to store the numbers.

# Test case
nums = [0, 3, 2, 4, 6, 1, 100, 45, 45, 47]
solution = Solution()
print(solution.longestConsecutive(nums))  # Expected output: 6, the longest consecutive sequence is [0, 1, 2, 3, 4, 6]


