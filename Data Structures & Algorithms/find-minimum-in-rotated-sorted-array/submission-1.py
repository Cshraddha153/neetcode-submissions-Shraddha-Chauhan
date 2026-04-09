class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        ans = nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                ans = min(ans, nums[l]) 
                break
            mid = (l + r)//2
            ans = min(ans, nums[mid])
            print(ans)
            if nums[l] <= nums[mid]:
                l = mid + 1
            else: # nums[r]>nums[mid]  left part me mi exists karega
                print("nums[l]", nums[l])
                print("nums[mid]", nums[mid])
                print("nums[r]", nums[r])
                print("mid", mid)
                r = mid - 1
        return ans

             