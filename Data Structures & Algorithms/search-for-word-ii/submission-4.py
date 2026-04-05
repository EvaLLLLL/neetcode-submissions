class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def prefix(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)

        visit = set()
        res, path = set(), []
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def backtrack(r, c, node):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            path.append(board[r][c])
            nextNode = node.children[board[r][c]]
            if nextNode.isEnd:
                res.add("".join(path))

            for dr, dc in DIRECTIONS:
                backtrack(r + dr, c + dc, nextNode)

            visit.remove((r, c))
            path.pop()

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, trie.root)
        
        return list(res)


        