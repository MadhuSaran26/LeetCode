class Node:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Solution:
    def buildTrie(self):
        for word in self.word_dict:
            node = self.trie
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.is_word = True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        self.word_dict = wordDict
        self.trie = Node()
        self.buildTrie()

        dp = [False] * n
        i = 0
        for i in range(n):
            if i==0 or dp[i-1]:
                node = self.trie
                for j in range(i, n):
                    c = s[j]
                    if c not in node.children:
                        break
                    node = node.children[c]
                    if node.is_word:
                        dp[j] = True
        
        return dp[-1]


        