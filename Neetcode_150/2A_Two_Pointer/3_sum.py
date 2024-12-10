"""
15. 3Sum

Medium

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
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
        # Step 1: Initialize result list to store unique triplets
        triplets = []

        # Step 2: Sort the input list to facilitate the two-pointer technique
        nums.sort()

        # Step 3: Iterate through the sorted list to find triplets
        for i in range(len(nums)):
            # Step 4: Skip duplicate elements to avoid considering the same triplet multiple times
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 5: Initialize two pointers: 
            # left_pointer starts just after i, and right_pointer starts at the end of the list
            left_pointer, right_pointer = i + 1, len(nums) - 1

            # Step 6: Use two pointers to find pairs that sum to -nums[i]
            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

                # Step 7: If the sum is greater than zero, move the right pointer to the left
                if current_sum > 0:
                    right_pointer -= 1
                # Step 8: If the sum is less than zero, move the left pointer to the right
                elif current_sum < 0:
                    left_pointer += 1
                else:
                    # Step 9: If the sum is zero, append the triplet to the result
                    triplets.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1

                    # Step 10: Skip duplicate elements for the left pointer to avoid adding the same triplet
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1

        # Step 11: Return the list of unique triplets
        return triplets

# Time Complexity:
# O(n^2), where n is the length of the input list. Sorting takes O(n log n), and the two-pointer iteration takes O(n) for each element.

# Space Complexity:
# O(1) for the space used by the algorithm, as the output space is not considered in the complexity.

# Test cases to validate the solution

# Test case 1: Multiple valid triplets
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