class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # TC = O(m+n∗2^n)  sc=O(m+2n)
        wordDict = set(wordDict)
        def solve(i):
            if i==len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    solve(j+1)
                    cur.pop()

        cur = []
        res=[]
        solve(0)
        return res