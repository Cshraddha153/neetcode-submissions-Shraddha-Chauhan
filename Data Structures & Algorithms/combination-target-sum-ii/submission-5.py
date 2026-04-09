class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # optimal
        res = []
        def backtrack(i, curr_sum, comb):
            if curr_sum == target:
                res.append(comb[::])
                return
            
            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                if curr_sum + nums[j] > target:
                    return
                comb.append(nums[j])
                backtrack(j+1, curr_sum+nums[j], comb)
                comb.pop()



        nums.sort()
        backtrack(0, 0, [])
        return res



        # tc=O(2^(t/m)) sc=O(2^(t/m))
        # res = []
        # def backtrack(i, curr_sum, comb):
        #     if curr_sum == target:
        #         res.append(comb[::])
        #         return
        #     if i>=len(nums) or curr_sum>target:
        #         return
            
        #     comb.append(nums[i])
        #     backtrack(i+1, curr_sum+nums[i], comb)
        #     comb.pop()
        #     while i+1<len(nums) and nums[i]==nums[i+1]:
        #         i+=1
        #     backtrack(i+1, curr_sum, comb)
        # nums.sort()
        # backtrack(0, 0, [])
        # return res

























        # res=[]
        # candidates.sort()
        # def backtrack(cur, pos, target):
        #     if target==0:
        #         res.append(cur.copy())
        #         return
        #     if target<=0:
        #         return
        #     prev=-1
        #     for i in range(pos, len(candidates)):
        #         if candidates[i]==prev:
        #             continue
        #         cur.append(candidates[i])
        #         backtrack(cur, i+1, target-candidates[i])
        #         cur.pop()
        #         prev = candidates[i]
        
        # backtrack([], 0, target)
        # return res

        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i==len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            # to avoid duplicate subset
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1   
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res

        