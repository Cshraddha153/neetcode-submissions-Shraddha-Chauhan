class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(n1):
            res=n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=1
            else:
                par[p1]=p2
                rank[p2]+=1
            return True

        par = [i for i in range(n)]
        rank = [1]*n
        count = n
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            else:
                count-=1
        return count == 1





        # tc=sc=O(V+E)  BFS soln + queue
        # if len(edges) > (n-1):
        #     return False

        # adj = [[] for i in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # q = deque([(0, -1)])
        # visit = set()
        # visit.add(0)
        # while q:
        #     node, par = q.popleft()
        #     for nei in adj[node]:
        #         if par == nei:
        #             continue
        #         if nei in visit:
        #             return False
        #         visit.add(nei)
        #         q.append((nei, node))      
                
        # return len(visit)==n 
   



        # tc=sc=O(V+E)  DFS + cycle detection
        # if len(edges) > (n-1):
        #     return False

        # visit = set()
        # def dfs(node, par):
        #     if node in visit:
        #         return False
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if par == nei:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # adj = [[] for i in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # print(adj)
        
                
        # return dfs(0, -1) and len(visit)==n 
   


                


























        
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