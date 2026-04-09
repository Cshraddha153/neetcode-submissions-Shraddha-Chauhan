class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res+=n%2  #0bit=0 1 bit=1
            n = n>>1 #right shift krdo bit ko divide by 2
        return res