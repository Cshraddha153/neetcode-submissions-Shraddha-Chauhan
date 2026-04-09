class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def Capture(r, c):
            if (r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O"):
                return
            board[r][c] = "P"
            Capture(r+1, c)
            Capture(r-1, c)
            Capture(r, c+1)
            Capture(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c]=="O" and (r in [0, ROWS-1] or c in [0, COLS-1])):
                    Capture(r,c)
                    print(board)
                
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="P":
                    board[r][c]="O"
               