class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MINHEAP PRIMS ALGO  tc=O(N^2 logn)  sc=O(N^2) 
        n = len(points)
        # adjacency list node and corresonding (cost, nei)
        adj = {i:[] for i in range(n)}
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distx = x2-x1
                disty = y2-y1
                cost = abs(distx) + abs(disty)
                
                adj[i].append([cost, j])
                adj[j].append([cost, i])

        # print(adj)
        visit = set()
        minHeap = [[0, 0]]
        res = 0
        while len(visit)<n:
            print(len(visit), minHeap)
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neicost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neicost, nei])
        
        return res
























        # N = len(points)
        # adj = {i:[] for i in range(N)}
        # for i in range(N):
        #     x1, y1 = points[i]
        #     for j in range(i+1, N):
        #         x2, y2 = points[j]
        #         dist = abs(x1-x2) + abs(y1-y2)
        #         adj[i].append([dist, j])
        #         adj[j].append([dist, i])
                
        # res = 0
        # visit = set()
        # minH = [[0, 0]]
        # while len(visit)<N:
        #     cost, i = heapq.heappop(minH)
        #     if i in visit:
        #         continue
        #     res+=cost
        #     visit.add(i)
        #     for neicost, nei in adj[i]:
        #         if nei not in visit:
        #             heapq.heappush(minH, [neicost, nei])
        # return res

