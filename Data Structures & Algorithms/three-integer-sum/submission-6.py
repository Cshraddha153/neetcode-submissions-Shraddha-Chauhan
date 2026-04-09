class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  TC=O(N^2) Sc=O(N)
        ans = []
        nums.sort()
        for i in range(len(nums)-2): #tc=O(N)
            if i>0 and nums[i]==nums[i-1]:
                continue
                #  two pointer approach tc=O(N)
            left, right = i+1, len(nums)-1
            while left<right:
                print(i, left, right)
                lets = nums[i]+nums[left]+nums[right]
                if lets==0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left-1]==nums[left]:
                        left+=1
                elif lets>0:
                    right-=1
                else:
                    left+=1
        return ans
                











        # tc=O(N3)  sc=O(m) m-> unique tripler  brute force
        # res = set()
        # nums.sort()
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))
        #                 print(res)
        # return [ans for ans in res]


























        # nums.sort()
        # res = []
        # for index, val in enumerate(nums):
        #     if index>0 and val == nums[index-1]:
        #         continue
        #     left, right =  index+1, len(nums)-1
        #     while left<right:
        #         curr_sum = val + nums[left] + nums[right]
        #         if curr_sum>0:
        #             right-=1
        #         if curr_sum<0:
        #             left+=1
        #         if curr_sum==0:
        #             res.append([val, nums[left], nums[right]])
        #             left+=1
        #             while left<right and nums[left]==nums[left-1]:
        #                 left+=1
        # return res








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