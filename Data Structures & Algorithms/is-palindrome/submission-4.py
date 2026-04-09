class Solution:
    def isPalindrome(self, s: str) -> bool:

        # T.C=O(n)  sc = O(n)
        ns = ""
        for c in s:
            if c.isalnum():
                ns+=c.lower()
        return ns==ns[::-1]




        # T.C=O(n)  sc = O(n)
        # s = s.lower()
        # print(s)
        # left, right = 0, len(s)-1
        # while left<right:
        #     while left<right and not s[left].isalnum():
        #         left+=1
        #     while left<right and not s[right].isalnum():
        #         right-=1
        #     if s[left]!=s[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
