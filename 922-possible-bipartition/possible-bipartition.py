class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = {idx:[] for idx in range(1, n+1)}

        for u,v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        color = dict()
        visited = set()

        def bfs(idx):
            queue = deque([idx])
            color[idx] = 1

            while queue:
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True  
        
        for idx in range(1, n+1):
            if idx not in color:
                if not bfs(idx):
                    return False 
        
        return True  