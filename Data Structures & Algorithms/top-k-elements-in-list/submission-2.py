class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for i in range(len(nums)+1)]

        for i, c in count.items():
            freq[c].append(i)
        
        print(freq)
        res = []
        for i in range(len(freq))[::-1]:

            for n in freq[i]:
                res.append(n)
                i-=1
                if len(res)==k:
                    return res
        return res







