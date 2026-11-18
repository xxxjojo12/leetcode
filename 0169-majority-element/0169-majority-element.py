class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for key, value in count.items():
            if value > len(nums) / 2:
                return key
        return 0
