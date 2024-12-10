"""
42. Trapping Rain Water

Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining. 

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        # Initialize two pointers: one at the start (left) and one at the end (right)
        left, right = 0, len(height) - 1
        
        # Initialize variables to track the maximum heights encountered so far from both sides
        left_max, right_max = height[left], height[right]
        
        # Variable to accumulate the total amount of water trapped
        water = 0

        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # If the height at the left pointer is less than the height at the right pointer,
            # we can only trap water by moving the left pointer
            if left_max < right_max:
                left += 1
                # Update the left_max to the maximum of the current left_max and height[left]
                left_max = max(left_max, height[left])
                # Add the trapped water at the current left position to the total water
                water += left_max - height[left]
            else:
                # If the height at the right pointer is less than or equal to the left pointer,
                # we can only trap water by moving the right pointer
                right -= 1
                # Update the right_max to the maximum of the current right_max and height[right]
                right_max = max(right_max, height[right])
                # Add the trapped water at the current right position to the total water
                water += right_max - height[right]

        # Return the total amount of trapped water
        return water

# Time Complexity:
# O(n), where n is the number of elements in the list `height`.
# We use two pointers, and each pointer moves at most n times, resulting in O(n) time complexity.

# Space Complexity:
# O(1), since we are using a constant amount of extra space for the pointers, max heights, and water variable.

# Test case
solution = Solution()
# Test case 1: No water trapped (ascending heights)
height1 = [0, 1, 2, 3, 4, 5]
# There are no dips between the bars, so no water can be trapped.
# Expected output: 0
print(solution.trap(height1))  # Expected output: 0

# Test case 2: No water trapped (descending heights)
height2 = [5, 4, 3, 2, 1, 0]
# There are no dips between the bars, so no water can be trapped.
# Expected output: 0
print(solution.trap(height2))  # Expected output: 0

# Test case 3: Water trapped between multiple bars
height3 = [3, 0, 2, 0, 4]
# Water is trapped between the bars at indices 1, 2, and 3.
# Expected output: 7
print(solution.trap(height3))  # Expected output: 7

# Test case 4: Only one bar
height4 = [1]
# Only one bar means no space for water to be trapped.
# Expected output: 0
print(solution.trap(height4))  # Expected output: 0

# Test case 5: Water trapped in a large valley
height5 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Water is trapped at multiple places: between bars at indices 1-2, 3-4, 5-6, etc.
# Expected output: 6
print(solution.trap(height5))  # Expected output: 6

# Test case 6: Multiple peaks and valleys
height6 = [4, 2, 0, 3, 2, 5]
# Water is trapped between bars at indices 1-2, and 3-4.
# Expected output: 9
print(solution.trap(height6))  # Expected output: 9

# Test case 7: All elements are the same
height7 = [3, 3, 3, 3, 3]
# No water can be trapped since all bars have the same height.
# Expected output: 0
print(solution.trap(height7))  # Expected output: 0

# Test case 8: Water trapped in a complex pattern
height8 = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1]
# Expected output: 10
print(solution.trap(height8))  # Expected output: 10

# Test case 9: Larger case
height9 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 2, 1, 3, 0, 2]
# Expected output: 16 (water trapped in several places)
print(solution.trap(height9))  # Expected output: 16
