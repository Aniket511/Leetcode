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

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in nums
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Create a list of empty lists to store numbers by their frequencies
        # freq[i] will hold all numbers that have a frequency of i
        freq = [[] for i in range(len(nums) + 1)]
        
        # Step 3: Populate the freq list, placing numbers in the corresponding frequency bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 4: Collect the top k frequent elements from the freq list (in reverse order)
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Start from the highest frequency
            for num in freq[i]:
                res.append(num)
                if len(res) == k:  # Once we've found k elements, return the result
                    return res

# Time Complexity:
# O(n), where n is the number of elements in `nums`. Counting frequencies takes O(n), and the rest of the steps 
# iterate over the numbers in the frequency list, which will also be O(n).

# Space Complexity:
# O(n), where n is the number of unique elements in `nums`. We store the frequency count and the frequency list.

# Test case
nums = [78, 78, 34, 34, 34, 20, 20, 20, 20, 20, 55, 55, 55, 55, 55]
k = 2
solution = Solution()
answer = solution.topKFrequent(nums, k)
print(answer)  # Expected output: [20, 55]

"""

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Create a frequency counter dictionary
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Create a min-heap of size k to store the top k frequent elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            # Ensure the heap size does not exceed k
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract the top k frequent elements from the heap
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res  # Return most frequent first

# Time Complexity:
# O(n log k), where n is the number of elements in `nums` and k is the number of top frequent elements to return.
# The frequency count takes O(n), inserting into the heap takes O(log k), and we perform this for all unique elements.

# Space Complexity:
# O(n), where n is the number of unique elements in `nums`. The counter dictionary and heap both store up to n elements.

# Test case
nums = [78, 78, 55, 55, 55, 20, 55, 55, 34, 34, 34, 20, 20, 20, 20]
k = 2
solution = Solution()
answer = solution.topKFrequent(nums, k)
print(answer)  # Expected output: [20, 55], because 20 and 55 are the two most frequent numbers

