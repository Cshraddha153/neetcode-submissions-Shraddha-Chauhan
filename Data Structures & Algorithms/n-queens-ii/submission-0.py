class Solution:
    def totalNQueens(self, n: int) -> int:
        # Backtracking (Hash Set)  Tc=O(n!)  sc=O(n)
        col = set()
        posdiag = set()
        negdiag = set()

        res = 0
        def solve(r):
            nonlocal res
            if r==n:
                res+=1
                return 
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                solve(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        solve(0)
        return res
