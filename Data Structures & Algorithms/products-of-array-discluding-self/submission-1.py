class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prev1 = 1
        for i in range(len(nums)):
            res[i]=prev1
            prev1 *= nums[i]
        print(res)
        prev2=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=prev2
            prev2 *= nums[i]

        return res

