class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if par == nei:
                    continue
                if not dfs(nei, node):
                    return False
            return True
                
        

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        print(adj)
        
                
        return dfs(0, -1) and len(visit)==n 
   


                


























        
        # if not n:
        #     return True
        # adj = {i:[] for i in range(n)}
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)
        
        # visit = set()

        # def dfs(i, prev):
        #     if i in visit:
        #         return False

        #     visit.add(i)
        #     for j in adj[i]:
        #         if j==prev:
        #             continue
        #         if not dfs(j, i):
        #             return False # cycle
                    
        #     return True

        # return dfs(0, -1) and len(visit) == n