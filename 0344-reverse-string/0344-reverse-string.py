class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s) // 2):
            temp = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = s[i]
            s[i] = temp