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
        #Solution 1 
        # Time Complexity O(nlogk)
        #
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res

        # #Solution 2
        # # Step 1: Count the frequency of each number
        # hashmap = {}
        # for element in nums:
        #     hashmap[element] = 1 + hashmap.get(element, 0)

        # # Step 2: Create a list of buckets based on frequency
        # array = [[] for numbers in range(len(nums) + 1)]
        # for key, value in hashmap.items():
        #     array[value].append(key)

        # # Step 3: Gather the top k frequent elements
        # result = []
        # for m in range(len(array) - 1, 0, -1):
        #     for num in array[m]:
        #         result.append(num)
        #         if len(result) == k:  # Stop when we have k elements
        #             return result
        
        # return result  # Return the result if less than k elements are found



nums = [78,78,34,34,34,20,20,20,20,20,55,55,55,55,55]
k = 2
solution = Solution()
answer = solution.topKFrequent(nums, k)
print(answer)