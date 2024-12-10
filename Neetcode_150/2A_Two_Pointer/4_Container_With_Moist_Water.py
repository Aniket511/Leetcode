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
In this case, the max area of water the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # Step 1: Initialize variable to keep track of the maximum area
        max_area = 0
        
        # Step 2: Initialize two pointers:
        # - left_pointer at the start (0th index)
        # - right_pointer at the end (last index)
        left_pointer, right_pointer = 0, len(heights) - 1

        # Step 3: Iterate while the left pointer is less than the right pointer
        while left_pointer < right_pointer:
            # Step 4: Calculate the area formed by the lines at left_pointer and right_pointer
            # The area is the width (right_pointer - left_pointer) times the smaller of the two heights
            current_area = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer])
            
            # Step 5: Update max_area if the current area is larger
            max_area = max(max_area, current_area)

            # Step 6: Move the pointer pointing to the smaller height inward to possibly increase the area
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        # Step 7: Return the maximum area found
        return max_area

# Time Complexity:
# O(n), where n is the number of elements in the input list. 
# We only iterate through the list once with the two-pointer technique.

# Space Complexity:
# O(1), since we only use a constant amount of extra space for variables like `max_area`, `left_pointer`, and `right_pointer`.

# Test cases to validate the solution

# Test case 1: Example with multiple possibilities
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution1 = Solution()
print(solution1.maxArea(height1))  # Expected output: 49

# Test case 2: Example with all heights the same
height2 = [1, 1, 1, 1, 1]
solution2 = Solution()
print(solution2.maxArea(height2))  # Expected output: 4

# Test case 3: Example with increasing height
height3 = [1, 2, 3, 4, 5]
solution3 = Solution()
print(solution3.maxArea(height3))  # Expected output: 6
