class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {parent:[] for parent in range(numCourses)}
        inorder = {child:0 for child in range(numCourses)}
        seen = set()
        ordered_list = []

        for child, parent in prerequisites:
            graph[parent].append(child)
            inorder[child] += 1
        
        source = deque([child for child in range(numCourses) if inorder[child]==0])

        while source:
            node = source.popleft()
            if node in seen:
                continue
            seen.add(node)
            ordered_list.append(node)

            for child in graph[node]:
                inorder[child] -= 1
                if inorder[child] == 0:
                    source.append(child)
        
        
        return ordered_list if len(ordered_list) == numCourses else []
        