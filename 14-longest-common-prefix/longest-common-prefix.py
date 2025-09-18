class Node:
    def __init__(self):
        self.children = dict()
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = Node()

    def addString(self, s):
        node = self.root
        for char in s:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isLast = True
    
    def checkString(self, s):
        node = self.root
        for char in s:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        trie = Trie()
        for s in strs:
            trie.addString(s)
        
        node = trie.root
        
        if len(node.children) > 1:
            return result

        while not node.isLast:
            if len(node.children) == 1:
                char = next(iter(node.children.keys()))
                result += char
                node = node.children[char]
            else:
                break
        
        return result


        



        