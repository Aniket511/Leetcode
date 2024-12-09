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
        left = 0
        right = len(height) - 1

        # Initialize variables to track the maximum heights encountered so far from both sides
        left_max = height[left]
        right_max = height[right]

        # Variable to accumulate the total amount of water trapped
        water = 0

        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # If the height at the left pointer is less than the height at the right pointer,
            # we can only trap water by moving the left pointer
            if left_max < right_max:
                left += 1
                # Update the left_max to the maximum value between the current left_max and height[left]
                left_max = max(left_max, height[left])
                # Add the trapped water at the current left position to the total water
                water += left_max - height[left]
            else:
                # If the height at the right pointer is less than or equal to the left pointer,
                # we can only trap water by moving the right pointer
                right -= 1
                # Update the right_max to the maximum value between the current right_max and height[right]
                right_max = max(right_max, height[right])
                # Add the trapped water at the current right position to the total water
                water += right_max - height[right]

        # Return the total amount of trapped water
        return water

# Test case 1: General example with multiple dips
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
solution1 = Solution()
print(solution1.trap(height1))  # Expected output: 6

# Test case 2: Example with no dips, should result in no water trapped
height2 = [4,2,3,1,2,1,5]
solution2 = Solution()
print(solution2.trap(height2))  # Expected output: 9

# Test case 3: Example where all heights are the same, no water can be trapped
height3 = [1,1,1,1,1]
solution3 = Solution()
print(solution3.trap(height3))  # Expected output: 0
