class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            subarray=1
            cur_sum=0
            for num in nums:
                cur_sum += num
                if cur_sum>largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    cur_sum = num
            return True
        
        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            m = (l+r)//2
            if cansplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res