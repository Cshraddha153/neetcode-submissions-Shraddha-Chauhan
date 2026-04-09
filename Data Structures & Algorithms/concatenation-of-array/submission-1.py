class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2*len(nums))
        for i, num in enumerate(nums):
            ans[i] = ans[i+len(nums)] = num
        return ans


        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

        # a = nums
        # b = nums
        # return a + b