"""
125. Valid Palindrome

Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Initialize two pointers, one starting at the beginning (left) and the other at the end (right) of the string.
        left, right = 0, len(s) - 1

        # Step 2: Loop until the left pointer is less than the right pointer
        while left < right:
            # Step 3: Skip over non-alphanumeric characters from the left side.
            # Move `left` to the right until it points to a valid alphanumeric character or `left` passes `right`.
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            
            # Step 4: Skip over non-alphanumeric characters from the right side.
            # Move `right` to the left until it points to a valid alphanumeric character or `right` passes `left`.
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1

            # Step 5: Compare the characters at the left and right pointers, ignoring case.
            # If they don't match, return False since it's not a palindrome.
            if s[left].lower() != s[right].lower():
                return False

            # Step 6: Move the pointers inward to continue checking the next characters.
            left += 1
            right -= 1

        # Step 7: If no mismatches were found, return True, meaning the string is a palindrome.
        return True
    
    # Step 8: Helper function to check if a character is alphanumeric.
    def isAlphanumeric(self, c: str) -> bool:
        # A character is alphanumeric if it is a letter (A-Z or a-z) or a digit (0-9).
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

# Test case 1: Palindrome with spaces and punctuation
s1 = "A man, a plan, a canal, Panama"
solution = Solution()
print(solution.isPalindrome(s1))  # Expected output: True

# Test case 2: Not a palindrome due to space and character mismatch
s2 = "race a car"
print(solution.isPalindrome(s2))  # Expected output: False

# Test case 3: Single character (always a palindrome)
s3 = "a"
print(solution.isPalindrome(s3))  # Expected output: True

# Test case 4: Empty string (always a palindrome)
s4 = ""
print(solution.isPalindrome(s4))  # Expected output: True

# Test case 5: Palindrome with only numbers
s5 = "12321"
print(solution.isPalindrome(s5))  # Expected output: True

# Test case 6: Non-palindrome with numbers
s6 = "12345"
print(solution.isPalindrome(s6))  # Expected output: False
