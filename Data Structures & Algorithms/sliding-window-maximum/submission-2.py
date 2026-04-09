class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        count3 = {}
        for i in range(k):
            count3[nums[i]] = 1 + count3.get(nums[i], 0)
        ans = []
        ans.append(max(count3))
        for r in range(k, len(nums)):
            print(max(count3))
            count3[nums[r]] = 1 + count3.get(nums[r], 0)
            count3[nums[l]] -= 1
            if count3[nums[l]] == 0:
                del count3[nums[l]]
            l+=1
            ans.append(max(count3))
        return ans
            