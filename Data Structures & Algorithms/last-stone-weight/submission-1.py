class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-ele for ele in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            if val1!=val2:
                heapq.heappush(stones, val1-val2)
        stones.append(0)
        return abs(stones[0])
            
