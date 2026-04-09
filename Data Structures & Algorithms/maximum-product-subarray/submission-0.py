class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        maxP, minP = 1, 1
        for n in nums:
            temp = maxP*n
            maxP = max(temp, n*minP, n)
            minP = min(temp, n*minP, n)
            res = max(res, maxP)
        return res