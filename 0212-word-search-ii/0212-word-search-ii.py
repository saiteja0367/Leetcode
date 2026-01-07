class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isEnd = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                node.isEnd = True

        # Build Trie
        trie = Trie()
        for w in words:
            trie.insert(w)

        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            # boundary + pruning checks
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEnd:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")

        return list(res)


        