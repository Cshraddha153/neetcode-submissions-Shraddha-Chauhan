class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
        sum2 = 0
        for i in range(len(nums)+1):
            sum2+=i
        return sum2-sum1
