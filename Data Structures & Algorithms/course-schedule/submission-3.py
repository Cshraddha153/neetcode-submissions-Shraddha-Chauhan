class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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





            
