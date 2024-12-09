"""
167. Two Sum II - Input Array Is Sorted

Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers: left (l) and right (r)
        left_pointer, right_pointer = 0, len(numbers) - 1

        # Loop until the pointers meet
        while left_pointer < right_pointer:
            # Calculate the current sum of the elements at the two pointers
            current_sum = numbers[left_pointer] + numbers[right_pointer]

            # If the sum is greater than the target, move the right pointer leftward to decrease the sum
            if current_sum > target:
                right_pointer -= 1
            # If the sum is less than the target, move the left pointer rightward to increase the sum
            elif current_sum < target:
                left_pointer += 1
            # If the sum is equal to the target, return the 1-based indices
            else:
                return [left_pointer + 1, right_pointer + 1]
        
        # Return an empty list if no such pair is found
        return []

# Test cases to validate the solution

# Test case 1: Normal case
numbers1 = [2, 7, 11, 15]
target1 = 9
solution1 = Solution()
print(solution1.twoSum(numbers1, target1))  # Expected output: [1, 2]

# Test case 2: Target sum is at the beginning of the list
numbers2 = [1, 2, 3, 4, 5]
target2 = 3
solution2 = Solution()
print(solution2.twoSum(numbers2, target2))  # Expected output: [1, 2]

# Test case 3: No valid pair
numbers3 = [1, 2, 3, 4, 5]
target3 = 10
solution3 = Solution()
print(solution3.twoSum(numbers3, target3))  # Expected output: []

# Test case 4: Target sum is at the end of the list
numbers4 = [1, 2, 3, 4, 6]
target4 = 10
solution4 = Solution()
print(solution4.twoSum(numbers4, target4))  # Expected output: [4, 5]