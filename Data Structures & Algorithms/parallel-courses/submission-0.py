class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indeg = [0] * (n + 1)
        adj = defaultdict(list)
        for pre, nxt in relations:
            indeg[pre] += 1
            adj[nxt].append(pre)

        q = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)

        finish = 0
        ans = 0
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                finish += 1
                for nei in adj[c]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            ans += 1
        
        return ans if finish == n else -1