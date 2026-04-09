class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # tc=O(logn)  sc=O(1)
        n = len(nums)
        def binary_search(left_bias):
            l, r = 0, n-1
            i = -1
            while l<=r:
                m = l + (r-l)//2
                if nums[m]>target:
                    r = m-1
                elif nums[m]<target:
                    l = m+1
                else:
                    i = m
                    if left_bias:
                        r = m-1
                    else:
                        l = m+1
            return i

        left = binary_search(True)
        right = binary_search(False)
        return [left, right]

        # res = [-1, -1]
        # for i, num in enumerate(nums):
        #     if num==target:
        #         if res[0] == -1:
        #             res[0] = res[1] = i
        #         else:
        #             res[1] = i
        # return res