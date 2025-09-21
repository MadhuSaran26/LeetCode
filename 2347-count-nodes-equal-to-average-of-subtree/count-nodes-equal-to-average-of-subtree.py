# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            curr_total = node.val + left[0] + right[0]
            curr_nodes = 1 + left[1] + right[1]
            if (curr_total // curr_nodes) == node.val:
                result += 1
            return [curr_total, curr_nodes]
        
        dfs(root)
        return result


        