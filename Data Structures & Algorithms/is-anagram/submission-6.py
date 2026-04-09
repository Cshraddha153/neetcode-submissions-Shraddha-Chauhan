class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tc=O(Nlogn)  sc=O(1)
        s = sorted(s)
        t = sorted(t)
        return s==t