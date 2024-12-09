"""
11. Container With Most Water

Medium

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize variable to keep track of the maximum area
        max_area = 0
        
        # Initialize two pointers: left pointer at the start and right pointer at the end of the list
        left, right = 0, len(height) - 1

        # Iterate while the two pointers do not cross each other
        while left < right:
            # Calculate the area formed by the lines at the left and right pointers
            # The area is the width (right - left) times the smaller height
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            # Move the pointer pointing to the smaller height to try and increase the area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # Return the maximum area found
        return max_area

# Test case 1: Example with multiple possibilities
height1 = [1,8,6,2,5,4,8,3,7]
solution1 = Solution()
print(solution1.maxArea(height1))  # Expected output: 49

# Test case 2: Example with all heights the same
height2 = [1,1,1,1,1]
solution2 = Solution()
print(solution2.maxArea(height2))  # Expected output: 4

# Test case 3: Example with increasing height
height3 = [1,2,3,4,5]
solution3 = Solution()
print(solution3.maxArea(height3))  # Expected output: 6
