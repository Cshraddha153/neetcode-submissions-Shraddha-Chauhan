class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # print("nums 1 =", nums)
        # Negative Marking  TC=O(N)  sc=O(1)
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0
        # print("nums 2 = ", nums)
            
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1<=val<=len(nums):
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1]==0:
                    nums[val-1] = -1*(len(nums)+1)
        # print("nums 3 = ", nums)
        
        for i in range(1, len(nums)+1):
            if nums[i-1]>=0:
                return i
        # print("nums 4 = ", nums)
        
        return len(nums)+1







        # tc=O(N2)   sc=O(1)
        # missing = 1
        # while True:
        #     flag = True
        #     for num in nums:
        #         if missing == num:
        #             flag = False
        #             break
            
        #     if flag:
        #         return missing
        #     missing+=1