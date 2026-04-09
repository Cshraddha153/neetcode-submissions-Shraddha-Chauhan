class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm (Recursion)
        # tc=O(ELOG(E))  sc=O(E)
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs('JFK')
        print(res)
        return res[::-1]




        # tc=sc=O(E*V)  DFS
        # adj = {src:[] for src, dest in tickets}
        # # print(adj)
        # tickets.sort()
        # for src, dest in tickets:
        #     adj[src].append(dest)
        # # print(adj)
        
        # res = ["JFK"]
        # def dfs(src):
        #     if len(res)==len(tickets)+1:
        #         return True
        #     if src not in adj:
        #         return False
        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v):
        #             return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False
        
        # dfs("JFK")
        # return res
                
























        
        # adj = {src:[] for src, dst in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)
        
        # res = ["JFK"]
        # def dfs(src):
        #     if len(res)==len(tickets)+1:    
        #         return True
        #     if src not in adj:
        #         return False
        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v): 
        #             return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res