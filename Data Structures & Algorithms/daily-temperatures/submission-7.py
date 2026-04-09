class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # [index, temp]
        res = [0]*len(temperatures)

        for index, val in enumerate(temperatures):
            while stack and stack[-1][0]<val:
                v, i = stack.pop()
                res[i] = (index-i)

            stack.append([val, index])
        return res