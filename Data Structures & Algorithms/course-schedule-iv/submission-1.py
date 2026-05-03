class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        indeg = [0] * numCourses
        is_pre = [[False] * numCourses for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].add(dst)
            indeg[dst] += 1
            is_pre[src][dst] = True

        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                for i in range(numCourses):
                    if is_pre[i][node]:
                        is_pre[i][nei] = True
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
            
        res = [is_pre[u][v] for u, v in queries]
        return res
