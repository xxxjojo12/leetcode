class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        # reversed nums2 [2, 4, 3, 1]
        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
            
            next_greater[i] = stack[-1] if stack else -1

            stack.append(i)

        # nums1 [4, 1, 2]
        return [next_greater[i] for i in nums1]
