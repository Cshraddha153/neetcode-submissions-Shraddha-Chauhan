class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman ford algo
        dist = [float('inf')]*n
        dist[src] = 0
        for i in range(k+1):
            print(i) 
            temp = dist[:]           
            for u, v, w in flights:
                if dist[u]==float('inf'):
                    continue
                if temp[v] > dist[u]+w: 
                    temp[v] = dist[u]+w
                    print(temp[v], dist[u]+w)
                    
            dist = temp[:]    
            print(dist)
        return dist[dst] if dist[dst]!=float('inf') else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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