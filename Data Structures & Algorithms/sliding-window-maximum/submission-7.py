class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        l=0
        for i in range(len(nums)):
            while q and nums[q[-1]]<nums[i]:
                q.pop()

            q.append(i)

            if l>q[0]:
                q.popleft()            
            if (i+1)>=k:
                ans.append(nums[q[0]])
                l+=1
        return ans

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        q = deque()  
        ans = []
        l=r=0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l+=1
            r+=1
        return ans
        


        