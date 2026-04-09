class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        print(freq)
        print(counts)
        for val, count in counts.items():
            freq[count].append(val)
        res = []
        print(freq)
        for values in freq[::-1]:
            print(values)
            for val in values:
                print(val)
                res.append(val)
                if len(res)==k:
                    return res
        return res
        
