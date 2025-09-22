# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seen_none = False

        while queue:
            node = queue.popleft()
            if not node:
                seen_none = True
            else:
                if seen_none:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        
        return True
        