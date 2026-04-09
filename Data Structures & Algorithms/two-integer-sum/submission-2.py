class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        return
        # map={}
        # for index, val in enumerate(nums):
        #     diff = target - val
        #     print(diff)
        #     if diff in map:
        #         return [map[diff], index]
        #     map[val] =  index
        # return



