class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, val in enumerate(nums):
            if index>0 and val == nums[index-1]:
                continue
            left, right =  index+1, len(nums)-1
            while left<right:
                curr_sum = val + nums[left] + nums[right]
                if curr_sum>0:
                    right-=1
                if curr_sum<0:
                    left+=1
                if curr_sum==0:
                    res.append([val, nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res








        # T.c=O(n3)  Sc=O(n)
        # res=set()
        # nums = sorted(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(temp))
        # print(res)                       
        # return [list(i) for i in res]