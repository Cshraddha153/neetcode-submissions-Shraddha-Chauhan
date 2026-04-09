class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 2) for _ in range(n)]
        for u, v, cst in flights: #sc=O(V+E) tc=O(E)
            adj[u].append([v, cst])
        
        dist[src][0] = 0
        q = [(0, src, -1)] # cost, node, stops
        while len(q): # heap size sc=O(n*k)  tc=O(N+K)*k we traverse n node and m edges k times atleast
            cost, node, stops = heapq.heappop(q)
            if dst == node:
                return cost
            if stops == k or dist[node][stops+1] < cost:
                continue
            for nei, w in adj[node]:
                nextCost = cost+w
                nextStops = 1 + stops
                if dist[nei][nextStops+1] > nextCost:
                    dist[nei][nextStops+1] = nextCost
                    heapq.heappush(q, (nextCost, nei, nextStops))
        return -1
        
        
        # Dijkstra algo TC = O(k × m × log n) m->edges processed
        # sc=  O(k × n + m)  ----> WRONG  <-----
        # adj = {i:[] for i in range(n)}
        # for u, v, w in flights:
        #     adj[u].append([v, w])
        
        # q = [(0, src, -1)] # cost, node and stops
        # visit = {}
        # while q:
        #     cost, node, stop = heapq.heappop(q)
        #     if node == dst:
        #         return cost
        #     if stop>=k:
        #         continue
        #     if node in visit and visit[node] <= stop:
        #         continue
        #     visit[node] = stop # if node is visted again with less node in between
            
        #     for nei, wt in adj[node]:
        #         if nei not in visit:
        #             heapq.heappush(q, (cost+wt, nei, stop+1))
        # return -1


        
        
        
        
        
        






        
        
        
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