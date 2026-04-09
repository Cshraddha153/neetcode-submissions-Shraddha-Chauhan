class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = [0]*26
        arr_t = [0]*26
        for i in range(len(s)):
            arr_s[ord(s[i])-ord('a')] += 1
            arr_t[ord(t[i])-ord('a')] += 1

        return arr_s==arr_t



        # tc=O(Nlogn)  sc=O(1)
        s = sorted(s)
        t = sorted(t)
        return s==t