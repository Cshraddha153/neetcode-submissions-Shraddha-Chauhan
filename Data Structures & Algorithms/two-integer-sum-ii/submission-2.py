class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left< right:
            curSum = nums[left]+nums[right]
            if curSum > target:
                right-=1
            if curSum<target:
                left+=1
            if curSum==target:
                return [left+1, right+1]
        return []



        # t.C=O(n)  sc=O(n)
        # map={}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in map:
        #         return [map[diff]+1, i+1]
        #     map[nums[i]] = i
        # return