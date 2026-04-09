class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for ele in nums:
            if ele in map:
                return True
            map[ele] = True
        return False

        # tc=O(N) it take n time to insert ele sc=O(N)
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


