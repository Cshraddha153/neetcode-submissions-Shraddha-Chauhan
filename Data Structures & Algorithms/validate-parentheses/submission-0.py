class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {"]":"[", "}":"{", ")":"("}

        for c in s:
            # case: c=']', '}', ')'
            if c in closetoopen:
                if stack and closetoopen[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
