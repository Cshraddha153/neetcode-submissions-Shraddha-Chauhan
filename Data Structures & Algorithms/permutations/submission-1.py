class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms




        # RECURSIVE  tc=O(N*N!)
        # if len(nums)==0:
        #     return [[]]
        # res = []
        # perms = self.permute(nums[1:])
        # for p in perms:
        #     for i in range(len(p)+1): # front nd back
        #        p_copy = p.copy()
        #        print("first = ",p_copy)
        #        p_copy.insert(i, nums[0])
        #        res.append(p_copy)
        #        print(p_copy)
        # return res
            























        # res = []
        # if len(nums)==1:
        #     return [nums[:]]

        # for i in range(len(nums)):
        #     n = nums.pop(0)
        #     perms = self.permute(nums)

        #     for term in perms:
        #         term.append(n)
    
        #     res.extend(perms)
        #     nums.append(n)
            
        # return res
