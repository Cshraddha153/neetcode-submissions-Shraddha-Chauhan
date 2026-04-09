class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # T.c=O(n)  S.C=O(n)
        q = collections.deque()
        l = r = 0
        output = []
        for r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            #remove left value from window
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output























        # T.C = O(n*k)   S.C = O(k)
        # l=0
        # count3 = {}
        # for i in range(k):
        #     count3[nums[i]] = 1 + count3.get(nums[i], 0)
        # ans = []
        # ans.append(max(count3))
        # for r in range(k, len(nums)):
        #     count3[nums[r]] = 1 + count3.get(nums[r], 0)
        #     count3[nums[l]] -= 1
        #     if count3[nums[l]] == 0:
        #         del count3[nums[l]]
        #     l+=1
        #     ans.append(max(count3))
        # return ans
            