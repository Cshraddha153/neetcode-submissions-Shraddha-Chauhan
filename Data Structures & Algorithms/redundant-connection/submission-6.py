class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return True
            elif rank[p1]>rank[p2]:
                rank[p1]+=1
                parent[p2] = p1
            else:
                rank[p2]+=1
                parent[p1] = p2
            return False
        
        parent = [i for i in range(len(edges)+1)]
        rank = [0]*(len(edges)+1)

        for u, v in edges:
            if union(u, v):
                return [u, v]
        return []
        










