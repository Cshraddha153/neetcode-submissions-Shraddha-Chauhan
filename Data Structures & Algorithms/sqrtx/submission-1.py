class Solution:
    def mySqrt(self, x: int) -> int:
        # tc=log(N)
        l, r = 0, x
        res = 0
        while l<=r:
            m = (l+r)//2
            if m*m>x:
                r = m-1
            elif m*m <x:
                l = m+1
                res = m
            else:
                return m
        return res














        # tc=O(N)
        if x==0:
            return 0
        
        res = 1
        for i in range(1, x+1):
            if i*i>x:
                return res
            res = i
        return res