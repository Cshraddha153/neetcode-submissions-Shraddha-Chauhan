class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        # print(list_values)
        heapq.heapify(maxHeap)
        time = 0
        q = deque() #(count, time)
        while q or maxHeap:
            time+=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt<0:
                    q.append([cnt, time+n])
            
            if q and time == q[0][1]:
                cnt, _ = q.popleft()
                heapq.heappush(maxHeap, cnt)           

        return time


