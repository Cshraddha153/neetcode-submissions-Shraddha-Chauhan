class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        n = len(words)
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]==w2[j]:
                    continue
                adj[w1[j]].add(w2[j])
                break

        res = []
        visit = {}

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei): # loop presen tif visit is true means char is in current path
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):#loop
                return ""
        
        res.reverse()
        return "".join(res)
























        
        # adj = {c: set() for w in words for c in w}
        
        # for i in range(len(words)-1):
        #     w1, w2 = words[i], words[i+1]
        #     minLen = min(len(w1), len(w2))
        #     if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
        #         return ""

        #     for j in range(minLen):
        #         if w1[j]!=w2[j]:
        #             adj[w1[j]].add(w2[j])
        #             break

        # visited = {}
        # res = []

        # def dfs(char):
        #     if char in visited:
        #         return visited[char]
                
        #     visited[char] = True

        #     for neighChar in adj[char]:
        #         if dfs(neighChar):
        #             return True
                
        #     visited[char] = False
        #     res.append(char)


        # for char in adj:
        #     if dfs(char):
        #         return ""    
        # res.reverse()
        # return "".join(res)












