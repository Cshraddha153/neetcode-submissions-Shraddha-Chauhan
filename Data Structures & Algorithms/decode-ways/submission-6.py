class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up soln
        dp = [0]*(len(s)+1)
        dp[len(s)]=1
        for i in range(len(s)-1, -1, -1):
            if s[i]=="0":
                dp[0]=0
            else:
                dp[i] = dp[i+1]
                if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                    dp[i] += dp[i+2]
            print(dp)
        return dp[0]





















        # top down memo tc=O(N)  sc=O(1)
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i>=len(s): # we decode it successfulyy
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     ans = dfs(i+1)
        #     if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
        #         ans += dfs(i+2)
        #     dp[i] = ans
        #     return ans

        # return dfs(0)




        # recursive soln tc=O(2^n) we have two choices can take 1 or 2 digit sc=O(N)-->recursive call stack
        # def dfs(i):
        #     if i>=len(s): # we decode it successfulyy
        #         return 1
        #     if s[i]=="0":
        #         return 0
        #     ans = dfs(i+1)
        #     if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
        #         ans += dfs(i+2)
           
        #     return ans

        # return dfs(0)


























        # dp = {len(s): 1}
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]

        #     if i + 1 < len(s) and (s[i] == "1" or
        #        s[i] == "2" and s[i + 1] in "0123456"
        #     ):
        #         dp[i] += dp[i + 2]
        # return dp[0]

        
        # dp = {len(s):1}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i]=="0":
        #         return 0
        #     res = dfs(i+1)
        #     if (i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
        #         res+=dfs(i+2)
        #     dp[i]=res
        #     return res

        # return dfs(0)