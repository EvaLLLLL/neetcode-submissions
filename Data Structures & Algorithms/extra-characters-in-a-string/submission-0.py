class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Build the trie from dictionary words
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)
        
        n = len(s)
        memo = {}  # More descriptive name than 'dp'
        memo[n] = 0  # Base case: no extra chars at end of string
        
        def dfs(start_idx):
            """Return minimum extra characters from position start_idx to end."""
            if start_idx in memo:
                return memo[start_idx]

            min_extra = 1 + dfs(start_idx + 1)
            
            current_node = trie.root
            for end_idx in range(start_idx, n):
                char = s[end_idx]
                if char not in current_node.children:
                    break
                
                current_node = current_node.children[char]
                if current_node.is_end:
                    min_extra = min(min_extra, dfs(end_idx + 1))
            memo[start_idx] = min_extra
            return min_extra
        
        return dfs(0)
