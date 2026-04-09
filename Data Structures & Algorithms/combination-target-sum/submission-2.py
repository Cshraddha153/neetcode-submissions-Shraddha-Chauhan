class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Optimal tc=O(2^(t/m)) sc=O(T/m)
        res = []
        nums.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total+nums[j])
                cur.pop()
            
        dfs(0, [], 0)
        return res








        # backtracking tc=O(2^(t/m)) sc=O(T/m)
        # res = []
        # def backtrack(i, checksum, comb):
        #     if checksum==target:
        #         res.append(comb[::])
        #         return
        #     if i>=len(nums) or checksum>target:
        #         return
            
        #     comb.append(nums[i])
        #     checksum+=nums[i]
        #     backtrack(i, checksum, comb) # we can take same ele unlimited
        #     comb.pop()
        #     checksum-=nums[i]
        #     backtrack(i+1, checksum, comb)
        
        # backtrack(0, 0, [])
        # return res

























        # res = []
        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return 
        #     if i>=len(nums) or total>target:
        #         return
        #     cur.append(nums[i])
        #     dfs(i, cur, total + nums[i]) 
        #     cur.pop()
        #     dfs(i+1, cur, total)

        # dfs(0, [], 0)
        # return res