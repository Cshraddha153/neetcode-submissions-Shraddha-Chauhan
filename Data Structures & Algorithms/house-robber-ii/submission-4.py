class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
            
        def solve(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob2, rob1+n)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(solve(nums[:-1]), solve(nums[1:]))