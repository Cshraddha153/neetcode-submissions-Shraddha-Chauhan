class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap tc=O(N)  sc=O(N)
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = 1
        return False

        # Brute Force sorting
        # # tc=O(Nlogn)  sc=O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False