"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        map = {}
        map[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in map:
                    map[nei] = Node(nei.val)
                    q.append(nei)
                map[cur].neighbors.append(map[nei])
        return map[node]
        














        # oldtonew = {}  # hashmap

        # def dfs(node):
        #     #base case if node already present
        #     if node in oldtonew:
        #         return oldtonew[node]
        #     #copy
        #     copy = Node(node.val)
        #     oldtonew[node] = copy
        #     #check neighbor 0f node
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))

        #     return copy


        # return dfs(node) if node else None










