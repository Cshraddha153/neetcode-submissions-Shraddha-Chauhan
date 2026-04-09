class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = height[0]
        rightmax = height[n-1]
        l, r = 0, n-1
        area = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax<rightmax:
                area+=leftmax-height[l]
                l+=1
            else:
                area+=rightmax-height[r]
                r-=1
        return area

























        # if not height: return 0
        # l, r = 0, len(height)-1
        # leftmax, rightmax = height[l], height[r]
        # res = 0
        # while l < r:
        #     if leftmax < rightmax:
        #         l+=1
        #         leftmax=max(leftmax, height[l])
        #         res+=leftmax-height[l]    
        #     else:
        #         r-=1
        #         rightmax=max(rightmax, height[r])
        #         res+=rightmax-height[r]
        # return res
















        
                 