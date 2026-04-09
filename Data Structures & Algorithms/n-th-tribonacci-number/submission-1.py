class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def solve(n):
            if n<=1:
                return n
            if n==2:
                return 1
            if n in dp:
                return dp[n]
            dp[n] = solve(n-2) + solve(n-1) + solve(n-3)
            return dp[n]
        return solve(n)