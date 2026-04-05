class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }
        indeg = { c: 0 for c in adj }

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break

        queue = deque([w for w in indeg if indeg[w] == 0])
        res = ""
        while queue:
            char = queue.popleft()
            res += char
            for nei in adj[char]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        if len(res) != len(adj):
            return ""
        
        return res
