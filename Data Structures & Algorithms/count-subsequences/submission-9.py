class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]        
        for j in range(len(s)+1):
            dp[len(t)][j] = 1
       
        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if s[j]==t[i]:
                    dp[i][j] = dp[i+1][j+1] + dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0] 





        # dp = {}
        # def dfs(i, j):
        #     if j==len(t):
        #         return 1
        #     if i>=len(s):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if s[i]==t[j]:
        #         dp[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
        #     else:
        #         dp[(i, j)] = dfs(i+1, j)
        #     return dp[(i, j)]
        # return dfs(0, 0)