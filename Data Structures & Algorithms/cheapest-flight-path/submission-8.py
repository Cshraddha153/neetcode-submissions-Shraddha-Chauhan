class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))
        
        heap = [(0, src, 0)]  # cost, node, stops
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue
            for nei, wt in adj[node]:
                heapq.heappush(heap, (cost + wt, nei, stops + 1))
        
        return -1
        
        
        # Dijkstra algo TC = O(k × m × log n) m->edges processed
        # sc=  O(k × n + m)
        adj = {i:[] for i in range(n)}
        for u, v, w in flights:
            adj[u].append([v, w])
        
        q = [(0, src, -1)] # cost, node and stops
        visit = {}
        while q:
            cost, node, stop = heapq.heappop(q)
            if node == dst:
                return cost
            if stop>=k:
                continue
            if node in visit and visit[node] <= stop:
                continue
            visit[node] = stop # if node is visted again with less node in between
            
            for nei, wt in adj[node]:
                if nei not in visit:
                    heapq.heappush(q, (cost+wt, nei, stop+1))
        return -1


        
        
        
        
        
        






        
        
        
        # Bellman ford algo tc=O(n+(E*k))  sc=O(N) m-> no. of flightsprices =  = [float('inf')]*n
        # prices = [float('inf')]*n
        # prices[src] = 0
        # for i in range(k+1):
        #     temp = prices[:]           
        #     for u, v, w in flights:
        #         if prices[u]==float('inf'):
        #             continue
        #         if temp[v] > prices[u]+w: 
        #             temp[v] = prices[u]+w
                    
        #     prices = temp[:]    
        #     print(prices)
        # return prices[dst] if prices[dst]!=float('inf') else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # prices = [float("inf")]*n
        # prices[src]=0
        # for i in range(k+1):
        #     tmpprice = prices.copy()
        #     for s, d, p in flights:
        #         if prices[s]==float("inf"):
        #             continue 
        #         if prices[s]+p < tmpprice[d]:
        #             tmpprice[d] = prices[s]+p
        #     prices = tmpprice
        # return -1 if prices[dst]==float("inf") else prices[dst]