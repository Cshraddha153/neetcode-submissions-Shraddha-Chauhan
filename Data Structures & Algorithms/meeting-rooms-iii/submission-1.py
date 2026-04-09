class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # tc=O(mlogm + mlogn)   sc=O(N)
        # Two Min-Heaps
        meetings.sort()
        avai = [i for i in range(n)]
        used = [] # (endtime, room no)
        count = [0]*n # meeting count of each room

        for s, e in meetings:
            while used and used[0][0]<=s:
                _, room = heapq.heappop(used)
                heapq.heappush(avai, room)
            if not avai:
                end_time, room = heapq.heappop(used)
                e = end_time + (e-s)
                heapq.heappush(avai, room)
            
            room = heapq.heappop(avai)
            heapq.heappush(used, (e, room))
            count[room]+=1

        return count.index(max(count))