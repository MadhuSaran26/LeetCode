# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        
        def dfs(node):
            if not node.left and not node.right:
                return [str(node.val)]
            left = dfs(node.left) if node.left else []
            right = dfs(node.right) if node.right else []
            curr = str(node.val)
            return [curr + prev for prev in left] + [curr + prev for prev in right]
        
        for num_str in dfs(root):
            result += int(num_str)
        
        return result

        


        