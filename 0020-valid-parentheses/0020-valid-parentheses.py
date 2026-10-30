class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in s:
            if i in check:
                stack.append(check[i])
            elif stack and stack[-1] == i:
                stack.pop()
            else:
                return False
        
        return not stack