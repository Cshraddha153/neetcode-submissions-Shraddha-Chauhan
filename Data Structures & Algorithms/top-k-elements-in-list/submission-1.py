class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

        # T.c=O(nlogn), S.c=O(n)
        # map = defaultdict(int)
        # for num in nums:
        #     map[num] += 1
        # num = sorted(map.keys(), key=lambda x: map[x], reverse=True)
        # return num[:k]
