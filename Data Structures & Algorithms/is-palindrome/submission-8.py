class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str+=c.lower()
        if new_str==new_str[::-1]:
            return True
        return False






















        l, r = 0, len(s)-1
        s = s.lower()
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        # T.c = O(n)   S.C = O(1)