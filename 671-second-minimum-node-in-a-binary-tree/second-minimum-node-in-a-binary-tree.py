# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return -1
        
        second = float('inf')
        
        def dfs(node):
            nonlocal second
            if not node:
                return
            if node.val > second:
                return
            if node.val != root.val:
                second = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return second if second != float('inf') else -1
            
        