class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = nums[0]
        while l<=r:
            m = (l+r)//2
            if nums[l]<nums[r]:
                return min(ans, nums[l])
                break
            ans = min(ans, nums[m])
            # left part is sorted
            if nums[l]<=nums[m]:
                l = m+1
            else: # right part sorted
                r = m-1
        return ans