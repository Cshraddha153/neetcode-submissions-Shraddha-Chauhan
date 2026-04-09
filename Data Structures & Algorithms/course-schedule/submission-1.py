class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit: 
                return True
            cycle.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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











