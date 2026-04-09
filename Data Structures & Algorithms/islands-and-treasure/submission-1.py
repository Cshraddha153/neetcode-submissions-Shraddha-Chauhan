class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        dist = 1
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc]==2147483647:
                        grid[nr][nc]=dist
                        q.append((nr, nc))
            dist+=1
