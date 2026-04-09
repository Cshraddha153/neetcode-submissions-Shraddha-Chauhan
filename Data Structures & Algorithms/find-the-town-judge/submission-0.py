class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # ndegree & Outdegree tc=O(V+E)  sc=O(V)
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src]+=1
            incoming[dst]+=1
        
        for i in range(1, n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1