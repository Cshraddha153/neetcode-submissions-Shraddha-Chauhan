class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # tc=O(M*N * 4^(len(word)))  sc=O(len(word))
        def backtrack(r, c, index):
            if len(word)==index:
                return True

            if r<0 or c<0 or r>=n or c>=m or (r, c) in visit or board[r][c] != word[index]:
                return False
            visit.add((r, c))
            
            res = (backtrack(r+1, c, index+1) or backtrack(r-1, c, index+1) or backtrack(r, c-1, index+1) or backtrack(r, c+1, index+1))
            visit.remove((r, c))
            return res

        visit = set()   
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                
                if backtrack(i, j, 0):
                    return True
        return False

























        # rows, cols = len(board), len(board[0])
        # path = set()
        # def dfs(r, c, i):
        #     if i == len(word):
        #         return True

        #     if ( r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
        #         return False

        #     path.add((r, c))
        #     res = (dfs(r+1, c, i+1) or
        #             dfs(r-1, c, i+1) or
        #             dfs(r, c+1, i+1) or
        #             dfs(r, c-1, i+1))
        #     path.remove((r,c))
        #     return res
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r, c, 0): return True
        
        # return False