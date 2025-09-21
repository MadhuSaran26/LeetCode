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
                return (0, 0)
            left_total, left_nodes = dfs(node.left)
            right_total, right_nodes = dfs(node.right)
            curr_total = node.val + left_total + right_total
            curr_nodes = 1 + left_nodes + right_nodes
            if (curr_total // curr_nodes) == node.val:
                result += 1
            return (curr_total, curr_nodes)
        
        dfs(root)
        return result


        