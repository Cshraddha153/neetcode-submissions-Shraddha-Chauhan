class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tc=O(N)  sc=O(N)
        map1 = {}
        for i in range(len(nums)):
            if target-nums[i] in map1:
                return [map1[target-nums[i]], i]
            map1[nums[i]] = i
        return []
            




        # # TC=O(N^2)  SC=O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
        # return -1
