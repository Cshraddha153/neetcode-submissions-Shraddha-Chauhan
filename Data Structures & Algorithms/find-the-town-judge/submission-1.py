class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # delta = incoming - outgoing == n-1
        delta = defaultdict(int)
        for src, dst in trust:
            delta[src]-=1
            delta[dst]+=1
        
        for i in range(1, n+1):
            if delta[i]==n-1:
                return i # it will be judge all rust on him but he wont trust on anybdy
        return -1


        # indegree & Outdegree tc=O(V+E)  sc=O(V)
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src]+=1
            incoming[dst]+=1
        
        for i in range(1, n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1