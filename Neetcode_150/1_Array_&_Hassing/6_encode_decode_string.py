"""
271. Encode and Decode Strings

Medium

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
"""

class Solution:
    
    def encode(self, strs: list[str]) -> str:
        # Step 1: Initialize an empty string `res` to store the encoded result.
        encoded_str = ""
        
        # Step 2: Iterate over the list `strs`
        for string in strs:
            # Step 3: For each string, append its length followed by a '#' and the string itself
            encoded_str += str(len(string)) + "#" + string
        
        # Return the encoded string
        return encoded_str

    def decode(self, s: str) -> list[str]:
        # Step 1: Initialize an empty list `res` to store the decoded strings
        decoded_strs = []
        index = 0  # Pointer to track current position in the string
        
        # Step 2: Iterate through the encoded string `s`
        while index < len(s):
            # Step 3: Find the position of the '#' character (hash_pos)
            hash_pos = index
            while s[hash_pos] != '#':
                hash_pos += 1
            
            # Step 4: Extract the length of the string (substring before '#')
            length = int(s[index:hash_pos])
            index = hash_pos + 1  # Move index past the '#' character
            
            # Step 5: Extract the substring of the specified length
            string = s[index:index + length]
            decoded_strs.append(string)
            
            # Move the index forward by the length of the current string
            index += length
        
        # Return the decoded list of strings
        return decoded_strs

# Time Complexity:
# encode: O(n), where n is the total number of characters in `strs`. We iterate over each string once.
# decode: O(n), where n is the length of the encoded string. We process each character in the string once.

# Space Complexity:
# encode: O(n), where n is the total number of characters in `strs`, since we store the result string.
# decode: O(n), where n is the length of the encoded string, as we store the decoded list.

# Test case
strs = ["leet", "code", "love", "you"]
solution = Solution()

# Encoding the list of strings
encoded_str = solution.encode(strs)
print("Encoded:", encoded_str)  # Expected output: "4#leet4#code4#love3#you"

# Decoding the encoded string
decoded_strs = solution.decode(encoded_str)
print("Decoded:", decoded_strs)  # Expected output: ["leet", "code", "love", "you"]