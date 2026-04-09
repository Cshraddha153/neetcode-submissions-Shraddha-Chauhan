class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Comparing adjacent words tc=O(N*M)  sc=O(1)
        order_index = {c:i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j==len(w2): # if word1 is bigger than word2 
                    return False
                
                if w1[j]!=w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True









        # tc=O(n*mlogn)  sc=O(n*m)  sorting
        order_index = {c:i for i, c in enumerate(order)}

        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)