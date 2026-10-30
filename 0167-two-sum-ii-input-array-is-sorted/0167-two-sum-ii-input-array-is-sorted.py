class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sub = target - numbers[r]
            if sub == numbers[l]:
                return [l + 1, r + 1]
            if sub > numbers[l]:
                l += 1
            elif sub < numbers[l]:
                r -= 1