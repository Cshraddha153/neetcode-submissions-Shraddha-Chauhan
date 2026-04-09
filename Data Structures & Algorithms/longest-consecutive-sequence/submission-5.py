class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force tc=O(N2)  sc=O(1)
        count = 0
        nums = set(nums)
        for ele in nums:
            temp = 1
            while ele+temp in nums:
                temp+=1
            count = max(count, temp)
        return count
                       
