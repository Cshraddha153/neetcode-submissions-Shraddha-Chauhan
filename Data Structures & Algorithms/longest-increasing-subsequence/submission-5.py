class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up tc=O(N^2)  sc=O(n^2)
        n = len(nums)
        LIS = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)
















        # top down approach with memoization 
        # tc=O(n^2) unique path ==> sc=O(n^2) cache 
        dp = {}
        def dfs(i, prev):
            if i>=len(nums):
                return 0 
            if (i, prev) in dp:
                return dp[(i, prev)]           
            incl = 0
            if nums[i]>prev:
                incl = 1 + dfs(i+1, nums[i])
            excl = dfs(i+1, prev)
            ans = max(incl, excl)
            dp[(i, prev)] = ans
            return ans
        dfs(0, float('-inf'))
        print(dp)
        return dfs(0, float('-inf'))


        # recursive tc=O(2^n)  at each index i have two choices to include it or not
        # sc=O(n)->recursive stack
        # def dfs(i, prev):
        #     if i>=len(nums):
        #         return 0            
        #     incl = 0
        #     if nums[i]>prev:
        #         incl = 1 + dfs(i+1, nums[i])
        #     excl = dfs(i+1, prev)
        #     ans = max(incl, excl)
        #     return ans
        
        # return dfs(0, float('-inf'))





























        # lis=[1]*len(nums)
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]<nums[j]:
        #             lis[i] = max(lis[i], 1+lis[j])
        # return max(lis)