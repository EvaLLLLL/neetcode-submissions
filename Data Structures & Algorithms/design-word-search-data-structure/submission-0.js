class TrieNode {
  constructor() {
    this.endOfword = false
    this.children = new Map()
  }
}

class WordDictionary {
  constructor() {
    this.root = new TrieNode()
  }

  addWord(word) {
    let curr = this.root

    for (const c of word) {
      if (!curr.children.has(c)) {
        curr.children.set(c, new TrieNode())
      }

      curr = curr.children.get(c)
    }

    curr.endOfword = true
  }

  search(word) {
    return this.dfs(word, 0, this.root)
  }

  dfs(word, j, root) {
    let curr = root

    for (let i = j; i < word.length; i++) {
      const c = word[i]

      if (c === ".") {
        for (const char of curr.children.keys()) {
          if (this.dfs(word, i + 1, curr.children.get(char))) {
            return true
          }
        }
        return false
      } else {
        if (!curr.children.has(c)) {
          return false
        }
        curr = curr.children.get(c)
      }
    }

    return curr.endOfword
  }
}
