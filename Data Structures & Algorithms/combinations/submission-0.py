class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        def solve(i, curr):
            if len(curr)==k:
                res.append(curr[:])
                return   
            if i >= n:
                return                         
            
            curr.append(nums[i])
            solve(i+1, curr)
            curr.pop()
            solve(i+1, curr)
        
        solve(0, [])
        return res