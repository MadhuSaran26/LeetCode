class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = {idx:[] for idx in range(1, n+1)}

        for u,v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        group1, group2 = set(), set()
        visited = set()

        def bfs(idx):
            queue = deque([idx])

            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in adj_list[node]:
                    if node in group1:
                        if neighbor in group1:
                            return False
                        if neighbor in group2:
                            continue
                        group2.add(neighbor)
                    elif node in group2:
                        if neighbor in group2:
                            return False
                        if neighbor in group1:
                            continue
                        group1.add(neighbor)
                    else:
                        group1.add(node)
                        group2.add(neighbor)
                    if neighbor not in visited:
                        queue.append(neighbor)
            return True  
        
        for idx in range(1, n+1):
            if idx not in visited:
                if not bfs(idx):
                    return False 
        return True  