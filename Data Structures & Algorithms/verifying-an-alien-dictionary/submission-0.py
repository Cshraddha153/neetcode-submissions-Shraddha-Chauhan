class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c:i for i, c in enumerate(order)}
        print("order_index : ", order_index)

        def compare(word):
            return [order_index[c] for c in word]
        print(words, sorted(words, key=compare))
        return words == sorted(words, key=compare)