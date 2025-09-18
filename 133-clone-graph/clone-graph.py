"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = dict()

        def dfs(root):
            if root in visited:
                return visited[root]
            cloned_root = Node(root.val)
            visited[root] = cloned_root
            for neighbor in root.neighbors:
                cloned_root.neighbors.append(dfs(neighbor))
            return cloned_root
        
        return dfs(node)

        