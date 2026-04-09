class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        dp ={}
        def solve(i, curr):
            if curr == target:
                return True
            if i>=len(nums) or curr>target:
                return False
            if (i, curr) in dp:
                return dp[(i, curr)]

            incl = solve(i+1, curr+nums[i])
            excl = solve(i+1, curr) 
            dp[(i, curr)] = incl or excl
            return dp[(i, curr)]

        return solve(0, 0)

        
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        target = sum(nums)//2
        for i in range(len(nums)-1, -1, -1):
            newdpset = set()
            for val in dp:
                if target == nums[i]+val:
                    return True
                newdpset.add(nums[i]+val)
                newdpset.add(val)
            dp = newdpset
        return False
        