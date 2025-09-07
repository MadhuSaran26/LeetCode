# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = deque([root, None])
        while len(queue) > 1:
            node = queue.popleft()
            if not queue[0]:
                result.append(node.val)
            if node:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
        
        return result