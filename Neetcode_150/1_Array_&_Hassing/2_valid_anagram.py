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
        if len(s) != len(t):
            return False

        count = [0] * 26
        for idx in range(len(s)):
            count[ord(s[idx]) - ord('a')] += 1
            count[ord(t[idx]) - ord('a')] -= 1

        for value in count:
            if value != 0:
                return False
        return True

s = "a"
t = "b"
solution = Solution()
print(solution.isAnagram(s, t))
