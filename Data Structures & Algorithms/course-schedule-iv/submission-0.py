class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Depth First Search (Hash Set)
        adj = defaultdict(list)
        for preq, crs in prerequisites:
            adj[crs].append(preq)
        
        def dfs(crs):
            if crs not in preq_map:
                preq_map[crs] = set()
                for pre_req in adj[crs]:
                    preq_map[crs] |= dfs(pre_req)
                preq_map[crs].add(crs)
            return preq_map[crs]
        
        preq_map = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in preq_map[v])
        return res