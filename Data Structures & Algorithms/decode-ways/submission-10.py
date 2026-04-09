class Solution:
    def numDecodings(self, s: str) -> int:
        # tc=scO(N)  bottom up approach
        dp = [0]*(len(s)+1)
        dp[len(s)]=1
        for i in range(len(s)-1, -1, -1):
            if s[i]=="0":
                dp[i] = 0
            else:
                dp[i]=dp[i+1]
            if i+1<len(s) and ((s[i]=="1") or (s[i]=="2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]











        # dp = {}
        # def dfs(i):
        #     if i>=len(s):
        #         return 1 if i==len(s) else 0
        #     if s[i]=="0":
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     ans = dfs(i+1)
        #     if i+1<len(s) and ((s[i]=="1") or (s[i]=="2" and s[i+1] in "0123456")):
        #         ans += dfs(i+2)
        #     dp[i] = ans
        #     return ans

        # return dfs(0)