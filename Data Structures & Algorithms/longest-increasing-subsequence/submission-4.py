class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
        
        return dfs(0, float('-inf'))



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