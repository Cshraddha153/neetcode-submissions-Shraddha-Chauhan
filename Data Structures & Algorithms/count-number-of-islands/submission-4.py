class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r, c) in visit or grid[r][c]=="0":
                return False
            visit.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return True
        
        visit = set()
        island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c):
                    island+=1
        return island