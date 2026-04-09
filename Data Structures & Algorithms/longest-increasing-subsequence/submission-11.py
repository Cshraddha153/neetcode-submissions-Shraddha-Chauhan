class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(2000)
        dp = {}
        def solve(i, prev):
            if i>= len(nums):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            # include
            incl = 0
            excl = solve(i+1, prev)
            if nums[i]>prev:
                incl = 1 + solve(i+1, nums[i])
            
            dp[(i, prev)] = max(incl, excl)
            return dp[(i, prev)]
            
        
        return solve(0, float('-inf'))
