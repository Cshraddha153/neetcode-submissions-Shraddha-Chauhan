class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # tc = (m*n) sc=O(M+N)  top down memoization
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            ans = 0
            if word1[i]==word2[j]:
                ans = dfs(i+1, j+1)
            else:
                ans = 1+min(dfs(i, j+1), dfs(i+1, j+1), dfs(i+1, j))
            dp[(i, j)] = ans
            return dp[(i, j)]
        
        return dfs(0, 0)


        # tc = 3^(m+n) (3 choices) sc=O(M+N)  (RECURISVE)
        def dfs(i, j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            ans = 0
            if word1[i]==word2[j]:
                ans = dfs(i+1, j+1)
            else:
                ans = 1+min(dfs(i, j+1), dfs(i+1, j+1), dfs(i+1, j))
            return ans
        
        return dfs(0, 0)
            

























        # cache = [[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]
        
        # for j in range(len(word2)+1):
        #     cache[len(word1)][j]=len(word2)-j

        # for i in range(len(word1)+1):
        #     cache[i][len(word2)]=len(word1)-i
       

        # for i in range(len(word1)-1, -1, -1):
        #     for j in range(len(word2)-1, -1, -1):
        #         if word1[i]==word2[j]:
        #             cache[i][j] = cache[i+1][j+1]
        #         else:
        #             cache[i][j]=1+min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])
        
        
        # return cache[0][0]
         