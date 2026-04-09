class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        print("dp", dp)
        for amountt in range(1, amount+1):
            for coin in coins:
                if (amountt-coin)>=0:
                    dp[amountt] = min(dp[amountt], 1+dp[amountt-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1