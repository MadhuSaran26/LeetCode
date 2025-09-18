class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        START, END = grid[0][0], grid[n-1][n-1]
        if START == 1 or END == 1:
            return -1
        directions = [(-1,0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queue = deque([(0,0)])
        grid[0][0] = 1

        while queue:
            crow, ccol = queue.popleft()
            distance = grid[crow][ccol]
            if (crow, ccol) == (n-1, n-1):
                return distance
            for dr, dc in directions:
                nr, nc = crow + dr, ccol + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = distance + 1
                    queue.append((nr, nc))
            
        return -1



        