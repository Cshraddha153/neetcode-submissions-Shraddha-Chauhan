# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def solve(root):
            nonlocal res
            if not root:
                return -1
            left = solve(root.left)
            right = solve(root.right)
            res = max(res, left+right+2)
            return 1 + max(left, right)
        solve(root)
        return res