class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Brute Force  tc=O(t*n)  sc=O(t)
        count = [0]*26
        for task in tasks:
            count[ord(task) - ord('A')] +=1
        
        arr = []
        for i in range(26):
            if count[i]>0:
                arr.append([count[i], i])
        
        time = 0
        processed = []
        while arr:
            maxi = -1
            for i in range(len(arr)):
                if all(processed[j] != arr[i][1] for j in range(max(0, time-n), time)):
                    if maxi == -1 or arr[maxi][0]<arr[i][0]:
                        maxi = i
            
            time+=1
            cur = -1
            if maxi != -1:
                cur = arr[maxi][1]
                arr[maxi][0] -= 1
                if arr[maxi][0]==0:
                    arr.pop(maxi)
            processed.append(cur)

        return time
        





        # # tc=O(T)--> no. of tasks and SC=O(1)
        # count = Counter(tasks)
        # maxHeap = [-val for val in count.values()]
       
        # heapq.heapify(maxHeap)
        # time = 0

        # q = deque() #(count, time)
        # while q or maxHeap:
        #     time+=1
        #     if maxHeap:
        #         cnt = 1 + heapq.heappop(maxHeap)
        #         if cnt<0:
        #             q.append([cnt, time+n])
            
        #     if q and time == q[0][1]:
        #         cnt, _ = q.popleft()
        #         heapq.heappush(maxHeap, cnt)           

        # return time


