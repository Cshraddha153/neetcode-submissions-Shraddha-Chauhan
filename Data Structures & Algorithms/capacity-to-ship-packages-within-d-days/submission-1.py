class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def canship(cap):
            ships, currcap  = 1, cap
            for w in weights:
                if currcap - w <0:
                    ships+=1
                    if ships>days:
                        return False
                    currcap = cap
                
                currcap-=w
            return True
        
        while l<=r:
            cap = (l+r)//2
            if canship(cap):
                res = min(res, cap)
                r = cap-1
            else:
                l = cap+1
        return res






        # # tc=O(N2) sc=O(1)
        # res = max(weights)

        # while True:
        #     ships=1
        #     cap = res
        #     for w in weights:
        #         if cap-w<0:
        #             ships+=1
        #             cap = res
        #         cap-=w
            
        #     if ships<=days:
        #         return res
            
        #     res+=1