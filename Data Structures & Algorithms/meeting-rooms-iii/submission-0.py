class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        available = [i for i in range(n)]
        heapq.heapify(available)

        working = [] # (endTime, index)
        meetingNums = [0] * n

        for start, end in meetings:
            # Release rooms that are free by the current meeting's start time
            while working and working[0][0] <= start:
                endTime, room = heapq.heappop(working)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                meetingNums[room] += 1
                heapq.heappush(working, (end, room))
            else:
                # No room available, wait for the earliest room to finish
                next_end, room = heapq.heappop(working)
                meetingNums[room] += 1
                # Delayed meeting duration remains the same
                heapq.heappush(working, (next_end + (end - start), room))

        # Find the room with max meetings and lowest index
        max_meetings = max(meetingNums)
        for i in range(n):
            if meetingNums[i] == max_meetings:
                return i