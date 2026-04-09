class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # two pointer aproach tc=O(n3)
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        return res

















        # n = len(nums)
        # nums.sort()
        # res = set()
        # for a in range(n):
        #     for b in range(a+1, n):
        #         for c in range(b+1, n):
        #             for d in range(c+1, n):
        #                 if nums[a]+nums[b]+nums[c]+nums[d]==target:
        #                     res.add((nums[a], nums[b], nums[c], nums[d]))
        # return list(res)