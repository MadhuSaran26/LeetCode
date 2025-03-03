class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n

        queue = deque([0])

        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            visited[node] = 1
            for neighbor in rooms[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
        
        return all(node == 1 for node in visited)
        