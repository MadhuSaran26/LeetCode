# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root, None])

        while len(queue)>0:
            node = queue.popleft()

            if len(queue)>=1 and queue[0] is None:
                result.append(node.val)
            
            if node:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
        
        return result