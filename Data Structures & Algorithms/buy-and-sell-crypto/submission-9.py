class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l=0
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l = r
        return profit




















        # dp tc=O(N) sc=O(1)
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP



        # # two pointer tc=O(N)  sc=O(1)
        # n = len(prices)
        # l, r = 0, 1
        # res = 0
        # while r<n:
        #     if prices[r]>prices[l]:
        #         res = max(res, prices[r]-prices[l])   
        #     else:
        #         l = r
        #     r+=1
        # return res




        # # brute force tc=O(N^2)  sc=O(1)
        # res = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[j]-prices[i] > res:
        #             res = prices[j]-prices[i]
        # return res