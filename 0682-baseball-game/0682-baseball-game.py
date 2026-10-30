class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ans = []

        for value in operations:
            match value:
                case "D":
                    ans.append(2 * ans[-1])
                case "C":
                    ans.pop()
                case "+":
                    ans.append(ans[-1] + ans[-2])
                case _:
                    ans.append(int(value))
        
        return sum(ans)
        

