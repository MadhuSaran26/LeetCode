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
        
        def buildGraph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                buildGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                buildGraph(node.right)
        
        buildGraph(root)

        #start from target to find the closest leaf
        queue = deque([k])
        visited = set()

        while queue:
            current = queue.popleft()
            visited.add(current)

            # the first leaf node (only its parent as its neighbor) from target is the answer
            # second condition is for cases with root which has only one child which is a leaf
            if len(graph[current]) == 1 and current != root.val:
                return current
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
            
        return -1

        