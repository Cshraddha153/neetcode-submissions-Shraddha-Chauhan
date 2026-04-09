class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # toposort kahns algo
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for s, d in prerequisites:
            indegree[d]+=1
            adj[s].append(d)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return finish == numCourses


        
        
        
        
        
        
        
        
        # dfs tc=sc=O(V+E)
        pre = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            pre[crs].append(preq)
        
        visit = set() # store the node currently we are visiting if we visit the 
        # same node twice it means we cant complete the crs
        def dfs(crs):
            if crs in visit:
                return False # cycle mil gyi
            if pre[crs]==[]:
                return True
                
            visit.add(crs)
            for preq in pre[crs]:
                if not dfs(preq):
                    return False
            visit.remove(crs)
            pre[crs]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True





            
