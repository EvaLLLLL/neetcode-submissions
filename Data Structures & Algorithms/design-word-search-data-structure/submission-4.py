class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)


    def _dfs(self, node: TrieNode, word: str, i: int) -> bool:
        if i == len(word):
            return node.isWord

        if word[i] == ".":
            for child_node in node.children.values():
                if self._dfs(child_node, word, i + 1):
                    return True
            return False
        else:
            if word[i] not in node.children:
                return False

            child_node = node.children[word[i]]
            return self._dfs(child_node, word, i + 1)
