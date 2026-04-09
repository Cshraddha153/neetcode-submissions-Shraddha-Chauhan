class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum2 = (n*(n+1))//2
        sum1 = sum(nums)
        # sum1=0
        # for i in range(len(nums)):
        #     sum1+=nums[i]
        # sum2 = 0
        # for i in range(len(nums)+1):
        #     sum2+=i
        return sum2-sum1
