class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for c in operations:

            if c == "+" and len(operations) > 2:
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif c == "C" and len(operations) > 0:
                stack.pop()
            elif c == "D" and len(operations) > 0:
                n = stack[-1]
                stack.append(n * 2)
            else:
                stack.append(int(c))
        
        for n in stack:
            sum += n

        return sum