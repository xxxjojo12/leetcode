class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        count = 0

        for val in hashmap.values():
            if val > 1:
                count += val * (val - 1) // 2

        return count