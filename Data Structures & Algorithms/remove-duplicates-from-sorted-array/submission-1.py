class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        print(nums, unique, len(unique))
        return len(unique)