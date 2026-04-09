class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force tc=O(N^2)  sc=O(1)
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res





        # prefix=1
        # res = [1]*len(nums)
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix*=nums[i]

        # suffix=1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i]*=suffix
        #     suffix*=nums[i]

        # return res

        # T.c= O(n)   S.c=O(n)






        