class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        group = defaultdict(list)      
        for s in strs:
            sorted_s = ''.join(sorted(s))
            print(sorted_s)
            group[sorted_s].append(s)
        return list(group.values())




        # hashtable tc=O(len(strs)*len(word)) sc=O(n)
        group = defaultdict(list)      
        for s in strs:
            key = [0]*26
            for char in s:
                key[ord(char)-ord('a')] += 1
            group[tuple(key)].append(s)
        return list(group.values())


