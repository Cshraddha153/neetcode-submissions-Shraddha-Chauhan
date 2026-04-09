class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                if pat not in dict:
                    dict[pat] = []
                dict[pat].append(word)
        
        q = deque()
        q.append(beginWord)
        visit = set()
        
        count = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return count
                
                for i in range(len(word)):
                    patt = word[:i] + "*" + word[i+1:]
                    for nei in dict[patt]:
                        if nei not in visit:
                            q.append(nei)

            count += 1
        
        return 0

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if endWord not in wordList:
        #     return 0
            
        # nei = collections.defaultdict(list)
        # wordList.append(beginWord)

        # for word in wordList:
        #     for j in range(len(word)):
        #         pattern = word[:j] + "*" + word[j+1:]
        #         nei[pattern].append(word)
           

        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
                
        #         if word == endWord:
        #             return res
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j+1:]
            
        #             for neiWord in nei[pattern]:
                        
        #                 if neiWord not in visit:
                            
        #                     visit.add(neiWord)
        #                     q.append(neiWord)

        #     res+=1

        # return 0




