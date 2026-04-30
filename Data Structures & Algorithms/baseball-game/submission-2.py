class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for c in operations:

            if c == "+" and len(operations) > 2:
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
                
            elif c == "C" and len(operations) > 0:
                res -= stack[-1]
                stack.pop()

            elif c == "D" and len(operations) > 0:
                res += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(c))
                res += int(c)


        return res