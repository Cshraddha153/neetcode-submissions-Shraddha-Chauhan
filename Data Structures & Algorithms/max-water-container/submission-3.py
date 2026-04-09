class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        area = 0
        while l<r:
            area = max(area, min(nums[l], nums[r])*(r-l))
            if nums[l]>nums[r]:
                r-=1
            else:
                l+=1
        return area
























        # tc=O(N)  sc=O(1)  two pointer
        area = 0
        l, r = 0, len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                area = max(area, heights[l]*(r-l))
                l+=1
            else:
                area = max(area, heights[r]*(r-l))
                r-=1
        return area





















        # brute force tc=O(N^2)  sc=O(1)
        area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = max(area, min(heights[i], heights[j])*(j-i))
        return area






















        # area = 0
        # left, right = 0, len(heights)-1
        # while left<right:
        #     temp = (right-left)*min(heights[left], heights[right])
        #     area = max(temp, area)
        #     if heights[left]<heights[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return area
                


        