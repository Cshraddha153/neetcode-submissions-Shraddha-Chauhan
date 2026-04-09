class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # tc=O(N^3)  sc=O(N^2)  bottom-up approach
        n = len(nums)
        arr = [1]+nums+[1]

        dp = [[0]*(n+2) for _ in range(n+2)]
        for l in range(n, 0, -1):
            for r in range(1, n+1):
                for i in range(l, r+1):
                    coins = arr[l-1]*arr[i]*arr[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]











        # tc=O(N^3)  sc=O(N^2)  Top-down approach
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l>r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                cost = nums[l-1]*nums[i]*nums[r+1]
                cost += dfs(l, i-1) + dfs(i+1, r) # i index exlude
                dp[(l, r)] = max(cost, dp[(l, r)])
            return dp[(l, r)]

        return dfs(1, len(nums)-2)








        # tc=O(N!)  sc=O(n)<--recursive depth  (TLE)
        def dfs(arr):
            if not arr:
                return 0
            max_cost = 0
            for i in range(len(arr)):
                left = arr[i-1] if i-1>= 0 else 1
                right = arr[i+1] if i+1<len(arr) else 1
                cost = left*arr[i]*right
                new_arr = arr[:i] + arr[i+1:]
                max_cost = max(max_cost, cost + dfs(new_arr))
            return max_cost

        return dfs(nums)































        # nums = [1] + nums + [1]
        # dp = {}
        # def dfs(l, r):
        #     if l>r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]
        #     dp[(l, r)] = 0
        #     for i in range(l, r+1):
        #         coins = nums[l-1]*nums[i]*nums[r+1]
        #         coins+=dfs(l, i-1)+dfs(i+1, r)
        #         dp[(l, r)]=max(dp[(l, r)], coins)
        #     return dp[(l, r)]
            
        # return dfs(1, len(nums)-2)