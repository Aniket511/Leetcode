"""
347. Top K Frequent Elements

Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Create a frequency counter dictionary
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        # Step 2: Create a max-heap based on the frequency of elements
        heap = []
        for key, val in counter.items():
            # Use negative frequency to simulate max-heap (Python's heapq is a min-heap by default)
            heapq.heappush(heap, (-val, key))
        
        # Step 3: Extract the top k frequent elements from the heap
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res

# Time Complexity:
# O(n log k), where n is the number of elements in `nums` and k is the number of top frequent elements to return.
# The frequency count takes O(n), building the heap takes O(n log k), and extracting k elements from the heap takes O(k log k).

# Space Complexity:
# O(n), where n is the number of unique elements in `nums`. The counter dictionary and heap both store up to n elements.

# Test case
nums = [78, 78, 34, 34, 34, 20, 20, 20, 20, 20, 55, 55, 55, 55, 55]
k = 2
solution = Solution()
answer = solution.topKFrequent(nums, k)
print(answer)  # Expected output: [20, 55], because 20 and 55 are the two most frequent numbers
