class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # DFS + binary search SOLN tc=O(n2*logn)  sc=O(N)
        n = len(grid)
        visit = [[False]*n for _ in range(n)]
        minH = grid[n-1][n-1]
        maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            # minH = min(minH, min(grid[row]))
        
        def dfs(i, j , t): # dfs tc=O(n^2)
            if min(i, j)<0 or max(i, j)>=n or grid[i][j]>t or visit[i][j]==True:
                return False
            visit[i][j] = True
            if i==n-1 and j==n-1:
                return True
            return (dfs(i+1, j, t) or dfs(i-1, j, t) or dfs(i, j+1, t) or dfs(i, j-1, t))
        
        ans = grid[0][0]
        while minH<=maxH:
            mid = (minH+maxH)//2
            if dfs(0, 0, mid):
                maxH = mid-1
                ans = mid
            else:
                minH = mid+1

            for i in range(n):
                for j in range(n):
                    visit[i][j] = False
        return ans

        



        # # DFS SOLN tc=O(n4)  sc=O(N)
        # n = len(grid)
        # visit = [[False]*n for _ in range(n)]
        # minH = grid[n-1][n-1]
        # maxH = grid[0][0]
        # for row in range(n):
        #     maxH = max(maxH, max(grid[row]))
        #     # minH = min(minH, min(grid[row]))
        
        # def dfs(i, j , t): # dfs tc=O(n^2)
        #     if min(i, j)<0 or max(i, j)>=n or grid[i][j]>t or visit[i][j]==True:
        #         return False
        #     visit[i][j] = True
        #     if i==n-1 and j==n-1:
        #         return True
        #     return (dfs(i+1, j, t) or dfs(i-1, j, t) or dfs(i, j+1, t) or dfs(i, j-1, t))
        
        # for t in range(minH, maxH+1): #tc=O(n^2)  t=n^2
        #     if dfs(0, 0, t):
        #         return t
        #     for i in range(n):
        #         for j in range(n):
        #             visit[i][j] = False
        # return 0
































        # DFS with Backtracking   BRUTE FORCE
        # all possible path and then find the best one
        # TC=O(4^n^2) it tries all paths N^2 sc=O(N^2) Call stack & visit set
        # visit = set()
        # n = len(grid)
        # def dfs(i, j, time):
        #     if i<0 or j<0 or i>=n or j>=n or (i, j) in visit:
        #         return float('inf')
    
        #     if i==n-1 and j==n-1:
        #         return max(time, grid[n-1][n-1])
        #     visit.add((i, j))
            
        #     time = max(grid[i][j], time)
        #     res = min(dfs(i+1, j, time), dfs(i-1, j, time), dfs(i, j+1, time), dfs(i, j-1, time))
        #     visit.remove((i, j))
        #     return res
        # return dfs(0, 0, grid[0][0])




















        # N = len(grid)
        # visit = set()
        # minH = [[grid[0][0], 0, 0]]
        # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # visit.add((0, 0))
        # while minH:
        #     t, r, c = heapq.heappop(minH)
        #     if r == N-1 and c==N-1:
        #         return t
        #     for dr, dc in directions: 
        #         neiR, neiC = r+dr, c+dc
        #         if (neiR<0 or neiC<0 or neiR==N or neiC==N or (neiR, neiC) in visit):
        #             continue
        #         visit.add((neiR, neiC))
        #         heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC]) 
