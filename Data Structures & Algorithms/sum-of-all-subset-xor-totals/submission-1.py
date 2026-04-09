class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Tc=O(n*2n)  sc=O(n)
        res = 0
        def solve(i, subset):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr^=num
            res+=xorr

            for j in range(i, len(nums)):
                subset.append(nums[j])
                solve(j+1, subset)
                subset.pop()
        solve(0, [])
        return res








        # def dfs(i, total):
        #     if i==len(nums):
        #         return total
        #     return dfs(i+1, total^nums[i]) + dfs(i+1, total)
        # return dfs(0, 0)