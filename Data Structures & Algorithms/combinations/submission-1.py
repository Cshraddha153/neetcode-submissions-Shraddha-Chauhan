class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = [i for i in range(1, n+1)]
        res = []
        def solve(i, curr):
            if len(curr)==k:
                res.append(curr[:])
                return   
            if i > n:
                return                         
            
            curr.append(i)
            solve(i+1, curr)
            curr.pop()
            solve(i+1, curr)
        
        solve(1, [])
        return res

    # TC = O(C(n, k)) 
    # sc=O(O(k) auxiliary + O(C(n, k) * k) output space)