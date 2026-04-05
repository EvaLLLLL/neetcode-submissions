class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        res = []

        for i, (enqueue_time, process_time) in enumerate(tasks):
            heapq.heappush(pending, (enqueue_time, process_time, i))

        time = 0
        while available or pending:
            while pending and pending[0][0] <= time:
                enqueue_time, process_time, i = heapq.heappop(pending)
                heapq.heappush(available, (process_time, i))

            if not available:
                time = pending[0][0]
                continue

            process_time, i = heapq.heappop(available)
            time += process_time
            res.append(i)
        return res
