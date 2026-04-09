class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force tc=sc=O(N2) O(N)
        res = 0
        store = set(nums)
        for num in nums:
            curr, streak = num, 0
            while curr+streak in store:
                streak+=1
            res = max(res, streak)

        return res





        # brute force tc=O(N)  sc=O(N)
        count = 0
        nums = set(nums)
        for ele in nums:
            temp = 1
            if ele-1 not in nums:
                while ele+temp in nums:
                    temp+=1
                count = max(count, temp)
        return count
                       
