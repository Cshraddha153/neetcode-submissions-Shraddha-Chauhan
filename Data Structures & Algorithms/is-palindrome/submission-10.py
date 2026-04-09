class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        def isalnum(c):
            asci_c = ord(c)
            return (ord('a')<= asci_c <= ord('z')) or (ord('A')<= asci_c <= ord('Z')) or (ord('0')<= asci_c <= ord('9'))
        
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not isalnum(s[l]):
                l+=1
            
            while l<r and not isalnum(s[r]):
                r-=1
            
            if s[l].lower() !=s[r].lower():
                return False
            l+=1
            r-=1
        return True











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