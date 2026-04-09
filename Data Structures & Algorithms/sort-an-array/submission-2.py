class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i]>right[j]:
                    merged.append(right[j])
                    j+=1
                else:
                    merged.append(left[i])
                    i+=1
                
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        def merge_sort(nums):
            if len(nums)==1:
                return nums
            m = len(nums)//2
            left = merge_sort(nums[:m])
            right = merge_sort(nums[m:])
            ans = merge(left, right)
            return ans

        # Merge sort (divide and conquer)
        # tc=O(Nlogn)  sc=O(N)   
        nums = merge_sort(nums)
        return nums









        
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