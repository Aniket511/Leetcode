class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res

nums = [7,6,6,7,8]
solution = Solution()
print(solution.singleNumber(nums))