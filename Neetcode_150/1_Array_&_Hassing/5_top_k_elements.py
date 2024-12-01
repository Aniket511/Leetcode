class Solution():
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each number
        hashmap = {}
        for element in nums:
            hashmap[element] = 1 + hashmap.get(element, 0)

        # Step 2: Create a list of buckets based on frequency
        array = [[] for numbers in range(len(nums) + 1)]
        for key, value in hashmap.items():
            array[value].append(key)

        # Step 3: Gather the top k frequent elements
        result = []
        for m in range(len(array) - 1, 0, -1):
            for num in array[m]:
                result.append(num)
                if len(result) == k:  # Stop when we have k elements
                    return result
        
        return result  # Return the result if less than k elements are found

nums = [1,2,2,3,3,3]
k = 2
solution = Solution()
answer = solution.topKFrequent(nums, k)
print(answer)