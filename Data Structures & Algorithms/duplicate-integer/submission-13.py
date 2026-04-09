class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset tc=O(N) sc=O(N)
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False

        # # hashmap tc=O(N)  sc=O(N)
        # map = {}
        # for num in nums:
        #     if num in map:
        #         return True
        #     map[num] = 1
        # return False

        # Brute Force sorting
        # # tc=O(Nlogn)  sc=O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False