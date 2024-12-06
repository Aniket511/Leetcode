class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize a list to store values since appending to a list is more efficient than a string
        merged = []

        # Initialize two pointers starting from 0 for indexing word1 and word2
        idx_1, idx_2 = 0, 0

        # While idx_1 and idx_2 are within bounds, append the characters from word1 and word2 alternately
        while idx_1 < len(word1) and idx_2 < len(word2):
            merged.append(word1[idx_1])
            merged.append(word2[idx_2])
            # Increment index positions
            idx_1 += 1
            idx_2 += 1

        # Append the rest of the characters from word1 and word2 (if any)
        merged.extend(word1[idx_1:])
        merged.extend(word2[idx_2:])

        # Join the list into a single string and return
        return "".join(merged)

word1 = 'abcde'
word2 = 'zyxwvutsr'
solution = Solution()
print(solution.mergeAlternately(word1, word2))
