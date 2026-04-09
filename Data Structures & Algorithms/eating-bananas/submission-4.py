class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l = 1 
        r = max(piles)
        while l<=r:
            mid = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours>h:
                l = mid+1
            else:
                ans = min(ans, mid)
                r= mid-1
        return ans





















        # l, r = 1, max(piles)
        # maxHour = r
        # while l<=r:
        #     k = (l + r)//2
        #     hour = 0 
        #     for p in piles:
        #         hour += math.ceil(p/k)
        #     if hour>h:
        #         l = k+1
        #     elif hour<=h:
        #         r = k - 1
        #         maxHour = min(maxHour, k)
        # return maxHour