class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force tc=O(N^2) sc-O(1)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        return -1





























    #     # T.C=O(n^2)   S.C=O(1)
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]+nums[j]==target:
    #                 return [i, j]
    #     return

    #     # T.C=O(n)   S.C=O(n)
    #     map={}
    #     for index, val in enumerate(nums):
    #         diff = target - val
    #         if diff in map:
    #             return [map[diff], index]
    #         map[val] =  index
    #     return



