class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
               
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count
        return dp[n][target]


        # dp = {}
        # def dfs(i, curr):
        #     if i>=len(nums):
        #         return 1 if curr==target else 0
        #     if (i, curr) in dp:
        #         return dp[(i, curr)]
        #     dp[(i, curr)] = dfs(i+1, curr+nums[i]) + dfs(i+1, curr-nums[i])
        #     return dp[(i, curr)]
        # return dfs(0, 0)