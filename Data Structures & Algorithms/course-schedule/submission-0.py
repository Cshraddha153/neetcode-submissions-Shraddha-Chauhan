class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            map[crs].append(preq)
        print(map)
        visitset = set()

        def dfs(crs):
            if crs in visitset:
                return False

            if map[crs]==[]:
                return True

            visitset.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    print("ookkk")
                    return False
            visitset.remove(crs)
            map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True











