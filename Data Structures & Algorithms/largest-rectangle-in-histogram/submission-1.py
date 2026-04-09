class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, hei = stack.pop()
                area = max(area, (i-index)*hei)
                start = index
            stack.append((start, h))

        for i, h in stack:
            area = max(area, (len(heights)-i)*h)

        return area





























        maxArea = 0
        stack = []  # [ind,val]
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                ind, val = stack.pop()
                maxArea = max(maxArea, h*(i-ind))
                start = ind
            
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
            
        return maxArea







