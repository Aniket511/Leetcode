"""
15. 3Sum

Medium

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and 
j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Initialize result list to store valid triplets
        res = []
        
        # Sort the input list to facilitate the two-pointer approach
        nums.sort()

        # Iterate through the sorted list
        for i in range(len(nums)):
            # Skip duplicate elements to avoid considering the same triplet multiple times
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers: one starts just after i (left pointer), and one at the end (right pointer)
            left_pointer, right_pointer = i + 1, len(nums) - 1

            # Use two pointers to find pairs that sum to the target value (-nums[i])
            while left_pointer < right_pointer:
                total = nums[i] + nums[left_pointer] + nums[right_pointer]

                # If the sum is greater than zero, move the right pointer to the left to decrease the sum
                if total > 0:
                    right_pointer -= 1
                # If the sum is less than zero, move the left pointer to the right to increase the sum
                elif total < 0:
                    left_pointer += 1
                else:
                    # If the sum is zero, append the triplet to the result
                    res.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1

                    # Skip duplicate elements for the left pointer to avoid adding the same triplet multiple times
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1

        # Return the list of triplets found
        return res

# Test case 1: Multiple triplets
nums1 = [-1, 0, 1, 2, -1, -4]
solution1 = Solution()
print(solution1.threeSum(nums1))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]

# Test case 2: No valid triplets
nums2 = [0, 1, 1]
solution2 = Solution()
print(solution2.threeSum(nums2))  # Expected output: []

# Test case 3: Only one valid triplet
nums3 = [0, 0, 0]
solution3 = Solution()
print(solution3.threeSum(nums3))  # Expected output: [[0, 0, 0]]
