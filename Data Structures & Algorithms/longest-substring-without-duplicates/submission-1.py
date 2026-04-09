class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        seen = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans = max(ans, r-l+1)
        return ans



























        # charset = set()
        # res = 0
        # left=0
        # for right in range(len(s)):
        #     while s[right] in charset:
        #         charset.remove(s[left])
        #         left+=1
        #     charset.add(s[right])
        #     res = max(res, right-left + 1)
        # return res 

        
        


        