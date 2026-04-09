class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        
        ans = []
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        print(q)
        finish = 0
        while q:
            node = q.popleft()
            ans.append(node)
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if finish!=numCourses:
            return []
        return ans[::-1]
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # preq = {i:[] for i in range(numCourses)}
        # for c, p in prerequisites:
        #     preq[c].append(p)
        # output = []
        # visit, cycle = set(), set()
        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     if crs in visit:
        #         return True
        #     cycle.add(crs)
        #     for pre in preq[crs]:
        #         if dfs(pre)==False:
        #             return False
        #     cycle.remove(crs)
        #     visit.add(crs)
        #     output.append(crs)
        #     return True

        # for c in range(numCourses):
        #     if dfs(c)==False:
        #         return []
        # return output
        