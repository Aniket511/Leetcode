class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)  # Convert list to a set for O(1) lookups
        longest_sequence = 0  # To keep track of the longest sequence found

        for number in nums:
            # If `number - 1` is not in the set, it means `number` is the start of a new sequence
            if number - 1 not in numset:
                current_sequence = 1  # Start with the current number as the first element in the sequence

                # Continue counting the sequence as long as the next number exists in the set
                while number + current_sequence in numset:
                    current_sequence += 1

                # Update the longest sequence if we found a longer one
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

nums = [0,3,2,4,6,1,100,45,45,47]
solution = Solution()
print(solution.longestConsecutive(nums))