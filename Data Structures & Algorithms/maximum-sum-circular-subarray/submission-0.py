class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for n in nums:
            curr_max = max(curr_max+n, n)
            curr_min = min(curr_min+n, n)
            total += n
            globalMax = max(globalMax, curr_max)
            globalMin = min(globalMin, curr_min)
            
        return max(globalMax, total-globalMin) if globalMax>0 else globalMax
