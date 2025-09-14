# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node, total):
            nonlocal result
            total = total*10 + node.val
            if not node.left and not node.right:
                result += total
            else:
                if node.left:
                    dfs(node.left, total)
                if node.right:
                    dfs(node.right, total)
        
        dfs(root, 0)
        
        return result

        


        