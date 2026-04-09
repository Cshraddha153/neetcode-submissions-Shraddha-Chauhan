class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap tc=O(Nlogn)  sc=(N)  sorting
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res







        # bucket sort tc=sc=O(N)
        counts = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for val, count in counts.items():
            freq[count].append(val)
        res = []       
        for values in freq[::-1]:
            for val in values:
                res.append(val)
                if len(res)==k:
                    return res
        return res
        
