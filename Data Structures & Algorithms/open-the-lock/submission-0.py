class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque(["0000"])
        visit = set()
        step = 0

        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return step

                visit.add(lock)
                for nxt in self._getNextLock(lock):
                    if (nxt not in visit) and (nxt not in dead):
                        visit.add(nxt)
                        q.append(nxt)
            step += 1
        return -1
    
    def _getNextLock(self, lock: str) -> List[str]:
        locks = []
        for i in range(4):
            d = int(lock[i])
            for move in [-1, 1]:
                nxt_digit = (d + move) % 10
                locks.append(lock[:i] + str(nxt_digit) + lock[i+1:])
        return locks
