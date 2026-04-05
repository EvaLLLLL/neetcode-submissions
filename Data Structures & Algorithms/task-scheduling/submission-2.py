class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        available = [-cnt for cnt in count.values()]
        heapq.heapify(available)
        
        pending = deque() # [-cnt, idleTime]

        time = 0
        while pending or available:
            time += 1

            if not available:
                time = pending[0][1]
            else:
                cnt = 1 + heapq.heappop(available)
                if cnt:
                    pending.append([cnt, time + n])
            
            if pending and pending[0][1] == time:
                heapq.heappush(available, pending.popleft()[0])
        
        return time
