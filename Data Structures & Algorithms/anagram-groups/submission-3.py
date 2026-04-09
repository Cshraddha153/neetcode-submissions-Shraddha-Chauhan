class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())




        # tc=O(m*n)=sc + O(m)
        map = defaultdict(list)
        for s in strs:
            char_count_array = [0]*26
            for i in range(len(s)):
                char_count_array[ord(s[i])-ord('a')] += 1
            count = tuple(char_count_array)
            map[count].append(s)
        return list(map.values())





















        # res = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     res[tuple(count)].append(s)
        # return res.values()