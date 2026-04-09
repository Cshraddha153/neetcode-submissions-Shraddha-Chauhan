class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []  # temp, index
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp, ind = stack.pop()
                res[ind] = (i-ind)
            stack.append([t, i])
        return res











        # l=0
        # ans = [0]*len(temperatures)
        # for r in range(1, len(temperatures)):
        #     right = r
        #     while right<len(temperatures):
        #         if temperatures[right]>temperatures[l]:
        #             ans[l] = (right-l)
        #             l+=1
        #             break
        #         right+=1
        # return ans
