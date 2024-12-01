class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for elements in nums:
            if elements in seen:
                return True
            seen.add(elements)
        return False

nums = [1,2,3,4,5]
solution = Solution()
print(solution.containsDuplicate(nums))

