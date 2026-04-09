class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r, c) in visit or grid[r][c]==0:
                return 0
            visit.add((r, c))           
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        visit = set()
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    ans=max(ans, dfs(r, c))
        return ans