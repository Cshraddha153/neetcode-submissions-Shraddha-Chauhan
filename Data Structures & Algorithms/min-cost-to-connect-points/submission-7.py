class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal algo always gives mst
        # tc=O(N^2logn) sc=O(N^2)bcoz of sorting O(ElogE)--> E=N^2
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1]+=1
            else:
                par[p1]=p2
                rank[p2]+=1
            return True

        n = len(points)
        rank = [1]*n
        par = [i for i in range(n)]
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                edges.append((dist, i, j))
        
        edges.sort()
    
        res = 0
        for dist, u, v in edges:
            if union(u, v):
                res += dist
        return res




        # MINHEAP PRIMS ALGO  tc=O(N^2)  sc=O(N)  optimal
        n, node = len(points), 0
        dist = [100000000]*n
        visit = [False]*n
        edges, res = 0, 0

        while edges < n-1:
            visit[node] = True
            nextNode = -1 # for which cost is min
            for i in range(n):
                if visit[i]:
                    continue

                curDist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                # print("i=", i, "nextNode=", nextNode,"dist =", dist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            node = nextNode
            edges+=1

        return res




        # MINHEAP PRIMS ALGO  tc=O(N^2 logn)  sc=O(N^2) 
        n = len(points)
        # adjacency list node and corresonding (cost, nei)
        adj = {i:[] for i in range(n)}
        for i in range(n-1):  # tc=sc=O(n^2)
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

