# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        if not root:
            return result
        
        def getHeight(node):
            nonlocal result
            if not node:
                return 0
            left = getHeight(node.left) 
            right = getHeight(node.right) 
            result = max(result, left + right)
            return max(left, right) + 1
        
        getHeight(root)
        return result

        