class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        num = sorted(map.keys(), key = lambda x: map[x], reverse=True)
        
        res = []
        return num[:k]
