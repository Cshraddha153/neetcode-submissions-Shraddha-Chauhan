class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        arr = []
        for x2, y2 in points:
            dist =(x2)**2 + (y2)**2
            arr.append(([dist, x2, y2]))
        heapq.heapify(arr)

        while k:
            _, x, y = heapq.heappop(arr)
            ans.append([x, y])
            k-=1

        return ans            