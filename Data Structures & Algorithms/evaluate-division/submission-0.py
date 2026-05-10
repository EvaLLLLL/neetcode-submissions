class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for equation, value in zip(equations, values):
            n1, n2 = equation
            adj[n1].append((n2, value))
            adj[n2].append((n1, 1.0 / value))

        def dfs(node, dst, visited):
            if node not in adj or dst not in adj:
                return -1.0
            if node == dst:
                return 1.0

            visited.add(node)
            for nextNode, value in adj[node]:
                if nextNode not in visited:
                    out = dfs(nextNode, dst, visited)
                    if out != -1.0:
                        return value * out
            
            return -1.0
            
        res = []
        for src, dst in queries:
            res.append(dfs(src, dst, set()))

        return res