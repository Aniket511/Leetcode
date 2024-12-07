"""
49. Group Anagrams

Medium

Given an array of strings strs, group the
anagrams
together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Step 1: Initialize a defaultdict of lists to store grouped anagrams
        # Each key will be a tuple representing the character count, and the value will be a list of words.
        hashmap = defaultdict(list)

        # Step 2: Iterate through each word in the input list `strs`
        for word in strs:
            # Step 3: Create a list `count` to keep track of the frequency of each letter in the word
            # We assume the words consist of lowercase English letters ('a' to 'z').
            count = [0] * 26  # A list with 26 zeros, one for each letter in the alphabet.
            
            # Step 4: Iterate through each letter in the word and update the frequency count
            for letter in word:
                count[ord(letter) - ord('a')] += 1  # Increment the count for the corresponding letter

            # Step 5: Use the tuple of the `count` list as the key in the hashmap.
            # Append the word to the list corresponding to that key.
            hashmap[tuple(count)].append(word)

        # Step 6: Return the grouped anagrams (the values of the hashmap as a list)
        return list(hashmap.values())  # Convert the hashmap values to a list and return

# Time Complexity:
# O(n * k), where n is the number of words in the input list `strs` and k is the average length of each word.
# For each word, we compute the frequency of each character (O(k)) and store it in a tuple (O(1) for each word).

# Space Complexity:
# O(n * k), where n is the number of words in `strs` and k is the average length of the words.
# We need space to store the frequency counts for each word and the resulting groups of anagrams.

# Test case
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
