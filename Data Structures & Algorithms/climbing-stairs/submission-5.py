class Solution:
    def climbStairs(self, n: int) -> int:
        # space optimized tc=O(N)  sc=O(1)
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp 
        return one






        # bottom up tc=sc=O(N)
        dp = [0]*(n+2)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1]+dp[i+2]
        return dp[0]




        # def dfs(i):
        #     if i==n:
        #         return 1
        #     if i>n:
        #         return 0
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)