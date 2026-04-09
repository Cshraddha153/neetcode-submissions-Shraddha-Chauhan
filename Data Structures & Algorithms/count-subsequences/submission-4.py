class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s), -1, -1):
            dp[i][len(t)] = 1
        print(dp)
        
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                dp[i][j] += dp[i+1][j+1] if s[i]==t[j] else 0
                dp[i][j] += dp[i+1][j]
        return dp[0][0]


        # top down soln tc=sc=O(m*n)  
        # dp = {}
        # def dfs(i, j):
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if j == len(t):
        #         return 1

        #     if i==len(s):
        #         return 0
    
        #     incl = 0
        #     if s[i] == t[j]:
        #         incl = dfs(i+1, j+1)
        #     excl = dfs(i+1, j)
        #     dp[(i, j)] = incl + excl
        #     return dp[(i, j)]
        # return dfs(0, 0)


        # tc=O(2^n)  sc=O(n)<-rescursive depth 
        # def dfs(i, j):
        #     if j == len(t):
        #         return 1

        #     if i==len(s):
        #         return 0
    
        #     incl = 0
        #     if s[i] == t[j]:
        #         incl = dfs(i+1, j+1)
        #     excl = dfs(i+1, j)
        #     ans = incl + excl
        #     return ans
        # return dfs(0, 0)

























        # cache ={}
        # def dfs(i, j):
        #     if j==len(t):
        #         return 1
        #     if i==len(s):
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     if s[i]==t[j]:
        #         cache[(i, j)]=dfs(i+1, j+1) + dfs(i+1, j)
        #     else: 
        #         cache[(i, j)]=dfs(i+1, j) 
        #     return cache[(i, j)]

        # return dfs(0, 0) 