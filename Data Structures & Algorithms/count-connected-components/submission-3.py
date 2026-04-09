# from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # bfs sol (queue)
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        count = 0
        for i in range(n):
            if i not in visit:
                q = deque([i])
                while q:
                    node = q.popleft()
                    visit.add(node)
                    for nei in adj[node]:
                        if nei not in visit:
                            q.append(nei)
                count +=1
        return count























        # dfs + stack good for large graph  No recurive depth exceeded problem
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(n): 
            stack = [n]   # <<<<<------------------
            while stack:
                node = stack.pop()  # <<<<<------------------
                visit.add(node)
                for nei in adj[node]:
                    if nei not in visit:
                        stack.append(nei)  # <<<<<------------------
            return 
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
        return count
            




        # dfs soln  tc=sc=O(V+E)  recursive depth = O(N)<-- we can reduce it using stack
        # adj = [[] for i in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # visit = set()
        # def dfs(node): 
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei not in visit:
        #             dfs(nei)
        #     return 
        
        # count = 0
        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         count+=1
        # return count
            

























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



