class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            for i, ele in enumerate(triplets[i]):
                if ele==target[i]:
                    ans.add(i)
        return True if len(ans)==3 else False