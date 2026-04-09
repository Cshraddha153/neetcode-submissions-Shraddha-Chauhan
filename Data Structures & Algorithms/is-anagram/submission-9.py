class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
        for ele, count in counts.items():
            t_count = countt.get(ele, 0)
            if t_count!= count:
                return False
        return True






















        count_s = Counter(s)
        count_t = Counter(t)
        for char in s:
            if count_s[char]!=count_t[char]:
                return False
        return True


        # Hash Table
        # # tc=O(N)  sc=O(1)
        # if len(s) != len(t):
        #     return False
        # arr_s = [0]*26
        # arr_t = [0]*26
        # for i in range(len(s)):
        #     arr_s[ord(s[i])-ord('a')] += 1
        #     arr_t[ord(t[i])-ord('a')] += 1

        # return arr_s==arr_t



        # tc=O(Nlogn)  sc=O(1)
        s = sorted(s)
        t = sorted(t)
        return s==t