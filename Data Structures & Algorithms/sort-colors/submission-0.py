class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l->0  i->1 r->2
        i, r = 0,  len(nums)-1
        l = 0
        while l<=r:
            if nums[l]==0:
                nums[i], nums[l] = nums[l], nums[i]
                i+=1
            elif nums[l]==2:
                nums[l], nums[r] = nums[r], nums[l]
                l-=1
                r-=1
            l+=1


            
        