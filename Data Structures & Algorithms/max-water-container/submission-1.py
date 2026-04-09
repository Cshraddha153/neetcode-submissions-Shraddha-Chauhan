class Solution:
    def maxArea(self, heights: List[int]) -> int:
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
                


        