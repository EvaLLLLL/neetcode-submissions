class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set("".join(words))
        adj = {c: set() for c in chars}
        indeg = {c: 0 for c in chars}

        for w1, w2 in zip(words, words[1:]):
            # invalid prefix: ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break

        q = deque([c for c in chars if indeg[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return "".join(res) if len(res) == len(chars) else ""