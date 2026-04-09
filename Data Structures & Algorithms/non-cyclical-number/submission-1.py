class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsq(num):
            digit = 0
            while num:
                digit += (num%10)**2
                num //=10
            return digit

        visit = set()
        while n not in visit:
            visit.add(n)
            n = sumofsq(n)
            if n==1:
                return True
        return False