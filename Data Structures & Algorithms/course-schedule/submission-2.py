class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort (Kahn's Algorithm) 
        # Tc=O(V+E)  sc=O(V+E)
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        
        q = deque()
        finish = 0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node = q.popleft()
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        print(finish)
        
        return finish==numCourses
        






        # DFS CYCLE DETCTION
        # adj = {i:[] for i in range(numCourses)} #tc=O(V+E)  sc=O(V+E)
        # for u, v in prerequisites:
        #     adj[u].append(v)

        # visit = set()
        # cycle = set()
        # def dfs(node):
        #     if node in cycle:
        #         return False
        #     if node in visit: 
        #         return True
        #     cycle.add(node)

        #     for nei in adj[node]:
        #         if not dfs(nei):
        #             return False
        #     cycle.remove(node)
        #     visit.add(node)
            
        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # map = {i:[] for i in range(numCourses)}
        # for crs, preq in prerequisites:
        #     map[crs].append(preq)
        # print(map)
        # visitset = set()

        # def dfs(crs):
        #     if crs in visitset:
        #         return False
        #     if map[crs]==[]:
        #         return True
        #     visitset.add(crs)
        #     for pre in map[crs]:
        #         if not dfs(pre):
        #             return False
        #     visitset.remove(crs)
        #     map[crs] = []
        #     return True

        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True











