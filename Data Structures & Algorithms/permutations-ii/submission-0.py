class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n]+=1
        
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        # tc=O(n!*n)=sc
        dfs()
        return res
                







        # # Backtracking (Hash Set)
        # # tc=O(n!*n)
        # res = set()
        # def backtrack(perm):
        #     if len(perm)==len(nums):
        #         res.add(tuple(perm))
        #         return
            
        #     for i in range(len(nums)):
        #         if nums[i]!=float('-inf'):
        #             perm.append(nums[i])
        #             nums[i] = float('-inf')
        #             backtrack(perm)
        #             nums[i] = perm[-1]
        #             perm.pop()
        
        # backtrack([])
        # return list(res)

