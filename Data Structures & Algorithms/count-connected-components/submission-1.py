class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node):
            # if node in visit:
            #     return 
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            return 
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
        return count
            

























        # par = [i for i in range(n)]
        # rank = [1]*n
        # def find(n1):
        #     res = n1
        #     while res!=par[res]:
        #         par[res] = par[par[res]]
        #         res = par[res]
        #     return res
        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     if p1 == p2:
        #         return 0
            
        #     if rank[p2]>rank[p1]:
        #         par[p1]=p2
        #         rank[p2]+=rank[p1]
        #     else:
        #         par[p2]=p1
        #         rank[p1]+=rank[p2]
        #     return 1
        
        # res = n
        # for n1, n2 in edges:
        #     res -= union(n1, n2)
        
        # return res



