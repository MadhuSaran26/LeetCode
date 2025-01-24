# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root.left and not root.right:
            return root.val
        
        graph = defaultdict(list)
        
        def buildGraph(node, parent=None):
            if not node:
                return
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)
        
        buildGraph(root.left, root)
        buildGraph(root.right, root)

        #start from target to find the closest leaf
        queue = deque([k])
        visited = set()
        root_val = root.val

        while queue:
            current = queue.popleft()
            visited.add(current)

            # the first leaf node (only its parent as its neighbor) from target is the answer
            # second condition is for cases with root which has only one child which is a leaf
            if len(graph[current]) == 1 and current != root_val:
                return current
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
            
        return -1

        