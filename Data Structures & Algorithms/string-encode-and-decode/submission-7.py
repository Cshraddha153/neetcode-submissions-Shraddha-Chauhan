class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0
        while r < len(s):
            j = r
            while s[r] != "#":
                r+=1
            length = int(s[j:r])
            res.append(s[r+1: r+length+1]) 
            r += length+1

        return res
