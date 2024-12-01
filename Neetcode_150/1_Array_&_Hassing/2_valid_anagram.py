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