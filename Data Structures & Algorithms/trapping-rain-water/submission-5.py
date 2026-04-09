class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]*len(height)
        maxright = [0]*len(height)
        maxleft_h = 0
        maxright_h = 0
        for i in range(1, len(height)):
            maxleft_h = max(maxleft_h, height[i-1])
            maxleft[i-1] = maxleft_h
        
        for i in range(len(height)-2, -1, -1):
            maxright_h = max(maxright_h, height[i+1])
            maxright[i+1] = maxright_h
        
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(maxleft[i], maxright[i]) - height[i])
        return ans
       
        # # tc=O(N)  sc=O(1)  two pointer
        # n = len(height)
        # leftmax = height[0]
        # rightmax = height[n-1]
        # l, r = 0, n-1
        # area = 0
        # while l<r:
        #     leftmax = max(leftmax, height[l])
        #     rightmax = max(rightmax, height[r])
        #     if leftmax<rightmax:
        #         area+=leftmax-height[l]
        #         l+=1
        #     else:
        #         area+=rightmax-height[r]
        #         r-=1
        # return area


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