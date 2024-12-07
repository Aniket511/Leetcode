"""
242. Valid Anagram

Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if both strings have the same length
        # If the lengths are different, they cannot be anagrams, so return False immediately.
        if len(s) != len(t):
            return False
        
        # Step 2: Create a list of 26 integers to track the frequency of each character.
        # We assume that the strings contain only lowercase English letters ('a' to 'z').
        count = [0] * 26

        # Step 3: Iterate over both strings simultaneously and update the frequency list.
        for idx in range(len(s)):
            # Increment the count for the character from string s
            count[ord(s[idx]) - ord('a')] += 1
            # Decrement the count for the character from string t
            count[ord(t[idx]) - ord('a')] -= 1
        
        # Step 4: After processing both strings, check if all counts are zero.
        # If any count is not zero, it means the strings are not anagrams (different frequencies).
        for value in count:
            if value != 0:
                return False
        
        # Step 5: If all counts are zero, the strings are anagrams of each other.
        return True

# Time Complexity:
# O(n), where n is the length of the strings s and t. 
# We iterate through both strings once, and updating the count array takes constant time (O(1)) for each character.

# Space Complexity:
# O(1), since the `count` array always has a fixed size of 26 (for each letter of the alphabet).
# The space used is constant regardless of the input size.

# Test case
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))  # Expected output: True (both are anagrams)

s2 = "rat"
t2 = "car"
solution = Solution()
print(solution.isAnagram(s2, t2))  # Expected output: False (not anagrams)


s = "a"
t = "b"
solution = Solution()
print(solution.isAnagram(s, t))
