# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        ans = 0
        while stack:
            node, hei = stack.pop()            
            if node:
                ans = max(ans, hei)
                stack.append([node.left, hei+1])
                stack.append([node.right, hei+1])

        return ans







        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))