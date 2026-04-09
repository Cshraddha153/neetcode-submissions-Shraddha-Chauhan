class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra algo (minheap) + Visit set()
        edges = {node:[] for node in range(1, n+1)}
        for u, v, t in times:
            edges[u].append([t, v])
        
        visit = set()
        q = [(0, k)] # time, node

        res = 0
        while q:
            t1, n1 = heapq.heappop(q)
            if n1 in visit:
                continue
            res=t1
            visit.add(n1)
            for t2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(q, (t1+t2, n2))
        
        return res if len(visit)==n else -1


        
        
        
        
        
        
        
        
        
        
        
        
        
        # DFS BAsed soln tc=O(V*E) avgcase tc=O(V+E)  sc=O(V+E) brute force dist array dic
        # adj = {i:[] for i in range(1, n+1)} #O(V)
        # for u, v, time in times: #O(E)  
        #     adj[u].append((v, time)) #O(V+E) to build adj time

        # dist = {node:float('inf') for node in range(1, n+1)}#IMPPP
                    
        # def dfs(node, time):
        #     if time >= dist[node]:
        #         return
        #     dist[node] = time
        #     for nei, tme in adj[node]: #O(V*E)
        #         dfs(nei, tme+time)
        
        # dfs(k, 0)
        # res = max(dist.values())
        # return res if res !=  float('inf') else -1
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # edges = collections.defaultdict(list)
        # for u, v, w in times:
        #     edges[u].append((v, w))
        
        # minHeap = [(0, k)]
        # visit = set()
        # t = 0
        # while minHeap:
        #     w1, n1 = heapq.heappop(minHeap)
        #     if n1 in visit:
        #         continue
        #     visit.add(n1)
        #     t = w1

        #     for n2, w2 in edges[n1]:
        #         if n2 not in visit:
        #             heapq.heappush(minHeap, (w1 + w2, n2))
        
        # return t if len(visit)==n else -1


        