class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort (minimum ele correct postion)
        # tc=O(N2)  sc=O(1)  (less swaps)
        for i in range(len(nums)):
            mini = i
            ele = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j]<ele:
                    mini = j
                    ele = nums[j]
            nums[i], nums[mini] = nums[mini], nums[i]
        return nums

        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums