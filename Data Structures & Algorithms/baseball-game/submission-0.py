class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c=="+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif c=="D":
                stack.append(2*stack[-1])
            elif c=="C":
                stack.pop()
            else:
                stack.append(int(c))
                
        return sum(stack)