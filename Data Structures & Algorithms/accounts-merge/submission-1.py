class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        p1, p2 =self.find(x1), self.find(x2)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=1
        else:
            self.par[p1] = p2
            self.rank[p2]+=1
        return True



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    uf.union(i, email_to_acc[e])
                else:
                    email_to_acc[e] = i
        
        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in email_to_acc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # tc == O((n∗m)log(n∗m))      DFS
        # n = len(accounts)
        # emailIdx = {} # email-->id
        # emails = []
        # emailToAcc = {} # email_index->account_id

        # m = 0
        # for accId, a in enumerate(accounts):
        #     for i in range(1, len(a)):
        #         email = a[i]
        #         if email in emailIdx:
        #             continue
        #         emails.append(email)
        #         emailIdx[email] = m
        #         emailToAcc[m] = accId
        #         m+=1
        
        # adj = [[] for _ in range(m)]
        # for a in accounts:
        #     for i in range(2, len(a)):
        #         id1 = emailIdx[a[i]]
        #         id2 = emailIdx[a[i-1]]
        #         adj[id1].append(id2)
        #         adj[id2].append(id1)
        
        # emailGroup = defaultdict(list) # index of acc --> list of emails

        # visited = [False]*m
        # def dfs(node, accId):
        #     visited[node] = True
        #     emailGroup[accId].append(emails[node])
        #     for nei in adj[node]:
        #         if not visited[nei]:
        #             dfs(nei, accId)
            
        # for i in range(m):
        #     if not visited[i]:
        #         dfs(i, emailToAcc[i])
        
        # res = []
        # for accId in emailGroup:
        #     name = accounts[accId][0]
        #     res.append([name]+sorted(emailGroup[accId]))
        
        # return res
            














