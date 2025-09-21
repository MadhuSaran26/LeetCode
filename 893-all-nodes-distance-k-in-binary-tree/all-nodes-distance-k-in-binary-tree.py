# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        visited = set()

        def addParent(node, parent):
            if not node:
                return
            node.parent = parent
            addParent(node.left, node)
            addParent(node.right, node)
        
        def backTrackNodes(node, distance):
            if not node or node in visited:
                return
            visited.add(node)
            if distance == 0:
                result.append(node.val)
                return
            backTrackNodes(node.left, distance - 1)
            backTrackNodes(node.right, distance - 1)
            backTrackNodes(node.parent, distance -1)

        addParent(root, None)
        backTrackNodes(target, k)
        return result
