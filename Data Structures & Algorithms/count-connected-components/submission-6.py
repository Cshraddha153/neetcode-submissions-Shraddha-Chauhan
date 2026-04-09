from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UNION FIND ALGORITHM 
        def find_parent(node):
            res = node
            while res != parent[res]: # if their is cycle in graph
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2: # cycle (irrelevant edge)
                return 0
            elif rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        parent = [i for i in range(n)]
        rank = [1]*n
        connected_comp = n
        for n1, n2 in edges:
            connected_comp -= union(n1, n2)
        
        return connected_comp

                
        



















        # bfs sol (queue)
        # adj = [[] for i in range(n)] 

        # for u, v in edges: # tc=O(E) sc=O(N+E)
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # visit = set()   #sc=O(N)
        # count = 0

        # # Overall  tc=O(V+E) sc=O(N+E)
        # for i in range(n):  # tc=O(N) 
        #     if i not in visit:
        #         q = deque([i])  #sc=O(N)
        #         while q:  # # tc=O(E) 
        #             node = q.popleft()
        #             visit.add(node)
        #             for nei in adj[node]:
        #                 if nei not in visit:
        #                     q.append(nei)
        #         count +=1
        # return count























        # dfs + stack good for large graph  No recurive depth exceeded problem
        # adj = [[] for i in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # visit = set()
        # def dfs(n): 
        #     stack = [n]   # <<<<<------------------
        #     while stack:
        #         node = stack.pop()  # <<<<<------------------
        #         visit.add(node)
        #         for nei in adj[node]:
        #             if nei not in visit:
        #                 stack.append(nei)  # <<<<<------------------
        #     return 
        
        # count = 0
        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         count+=1
        # return count
            




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



