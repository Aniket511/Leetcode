class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], idx]
            else:
                hashmap[val] = idx

nums = [2,7,11,15]
target = 26
soltion = Solution()
print(soltion.twoSum(nums, target))