class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count, counts = {}, {}
        for i in range(len(t)):
            count[t[i]] = 1 + count.get(t[i], 0)
        
        have, need = 0, len(count)
        l, r = 0, 0
        res = [-1, -1]
        max_len = float('inf')
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if s[r] in count and count[s[r]] == counts[s[r]]:
                have+=1
            
            while have==need:
                if r-l+1 < max_len:
                    res = [l, r]
                    max_len = r-l+1

                counts[s[l]]-=1
                if s[l] in count and counts[s[l]] < count[s[l]]:
                    have-=1
                l+=1
        
        l, r = res
        return s[l: r+1] if len(res) != float('inf') else ""






























        if t == "": return ""

        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, reslen = [-1, -1], float('infinity')
        l=0
        have, need = 0, len(countT)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have+=1
            
            while have == need:
                if (r-l+1)<reslen:
                    res = [l, r]
                    reslen = r-l+1
                
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
                
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""











