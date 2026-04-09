class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count = {}

        for i in range(len(hand)):
            count[hand[i]] = 1 + count.get(hand[i], 0)
        
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if len(hand)%groupSize:
            return False
        count = {}
        for n in hand:
            count[n]=1+count.get(n, 0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first  = minH[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True