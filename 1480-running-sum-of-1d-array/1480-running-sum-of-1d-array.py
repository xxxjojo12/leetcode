class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        carry = 0

        for i in range(len(nums)):
            nums[i] += carry
            carry = nums[i]

        return nums