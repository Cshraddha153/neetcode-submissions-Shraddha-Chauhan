class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = prod
            prod*=nums[i]

        # ans = [1, 1, 2, 8]
        div = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= div
            div *= nums[i]        
        return ans
