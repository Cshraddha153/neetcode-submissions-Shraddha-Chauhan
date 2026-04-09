class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        # nums = [-ele for ele in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) != self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
