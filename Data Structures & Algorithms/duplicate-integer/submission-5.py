class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(s)
        if len(s) != len(nums):
            return True
        return False






















        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        #     print(hashset)
        # return False


