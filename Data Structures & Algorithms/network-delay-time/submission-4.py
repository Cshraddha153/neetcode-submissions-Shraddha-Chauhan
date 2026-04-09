class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for u, v, time in times:
            adj[u].append((v, time))

        dist = {node:float('inf') for node in range(1, n+1)}#IMPPP
                    
        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for nei, tme in adj[node]:
                dfs(nei, tme+time)
        
        dfs(k, 0)
        res = max(dist.values())
        return res if res !=  float('inf') else -1
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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


        