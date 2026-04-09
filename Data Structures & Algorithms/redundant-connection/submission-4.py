class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       
        # DFS SOLUTION  brute force soln
        # tc=O(E*(V+E))  sc=O(V+E)

        # n = len(edges)+1
        # adj = [[] for i in range(n)]

        # def dfs(u, par):
        #     visit.add(u)
        #     for nei in adj[u]:
        #         if nei == par:
        #             continue  
        #         # node you gonna visit should be visited and should not be parent node
        #         if nei in visit or dfs(nei, u): # redundant connection
        #             return True
        #     return False
        
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        #     visit = set()
        #     if dfs(u, -1):
        #         return [u, v]
        # return []










        #  topological sort
        # tc=O(V+E)  sc=O(V+E)
        n = len(edges)+1
        adj = [[] for i in range(n)]
        indegree = [0]*n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            indegree[u]+=1
            indegree[v]+=1
        
        q = deque()
        for i in range(1, n):
            if indegree[i]==1:
                q.append(i)
        
        while q:
            node = q.popleft()
            indegree[node]-=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)
        
        for u,v in reversed(edges):
            if indegree[u]==2 and indegree[v]:
                return [u,v]

        return []
















        # TC = O(V+(E*ALPHA(V))) <-- amortized complexity (faster, path compression)
        # sc=O(V)

        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(n1):
            temp = n1
            while temp != parent[temp]:  # optimization
                parent[temp] = parent[parent[temp]]
                temp = parent[temp]
            return temp
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=1
            else:
                parent[p1] = p2
                rank[p2]+=1
            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
        return [] 
























        # par = [i for i in range(len(edges)+1)]
        # rank = [1]*(len(edges)+1)
        # def find(n):
        #     p = par[n]
        #     while p!=par[p]:
        #         par[p] = par[par[p]]
        #         p = par[p]
        #     return p
        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     if p1==p2:
        #         return False
        #     if rank[p1]>rank[p2]:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     else:
        #         par[p1] = p2
        #         rank[p2] += rank[p1]
        #     return True
        
        # for n1, n2 in edges:
        #     if not union(n1, n2):
        #         return [n1, n2]




                