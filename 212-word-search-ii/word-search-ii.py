class Node:
    def __init__(self):
        self.children = dict()
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isLast = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        numRows, numCols = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited, result = set(), []
        trie = Trie()

        for word in words:
            trie.addWord(word)

        def backtracking(node, sr, sc, path):
            if node.isLast and node not in visited:
                result.append(path)
                visited.add(node)

            temp = board[sr][sc]
            board[sr][sc] = "#"

            for dr, dc in directions:
                nr, nc = sr+dr, sc+dc
                if 0 <= nr < numRows and 0 <= nc < numCols and board[nr][nc] in node.children:
                    backtracking(node.children[board[nr][nc]], nr, nc, path + board[nr][nc])
            
            board[sr][sc] = temp
        
        for row in range(numRows):
            for col in range(numCols):
                if board[row][col] in trie.root.children:
                    backtracking(trie.root.children[board[row][col]], row, col, board[row][col])
        
        return result



        