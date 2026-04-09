# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level








        # stack = [[root, 1]]
        # ans = 0
        # while stack:
        #     node, hei = stack.pop()          
        #     if node:
        #         ans = max(ans, hei)
        #         stack.append([node.left, hei+1])
        #         stack.append([node.right, hei+1])

        # return ans







        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))