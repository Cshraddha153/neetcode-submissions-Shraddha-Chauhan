class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer tc=O(N)  sc=O(1)
        n = len(prices)
        l, r = 0, 1
        res = 0
        while r<n:
            if prices[r]>prices[l]:
                res = max(res, prices[r]-prices[l])   
            else:
                l = r
            r+=1
        return res




        # # brute force tc=O(N^2)  sc=O(1)
        # res = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[j]-prices[i] > res:
        #             res = prices[j]-prices[i]
        # return res