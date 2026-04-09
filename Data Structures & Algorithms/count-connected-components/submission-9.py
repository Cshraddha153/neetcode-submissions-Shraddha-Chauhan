class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # TC=O(V+E*alpha(V))
        # sc=O(V)
        def find(n):
            if n!=parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return False
            elif rank[p1]>rank[p2]:
                rank[p1]+=1
                parent[p2] = p1
            else:
                rank[p2]+=1
                parent[p1] = p2
            return True
        
        parent = [i for i in range(n)]
        rank = [0]*n
        res = n
        for u, v in edges:
            if union(u, v):
                res-=1
        return res
