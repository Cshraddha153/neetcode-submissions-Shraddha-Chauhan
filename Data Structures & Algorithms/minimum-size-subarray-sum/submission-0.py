class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding Window TC=O(N)  SC=O(1)
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total+=nums[r]
            while total >= target:
                res = min(r-l+1, res)
                total-=nums[l]
                l+=1
        return 0 if res==float('inf') else res