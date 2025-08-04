class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        directions = [(-1, 0), (0,1), (1,0), (0, -1)]
        visited = set()
        number_islands = 0

        def bfs(node):
            queue = deque([node])
            while queue:
                curr_row, curr_col = queue.popleft()
                if (curr_row, curr_col) in visited:
                    continue
                visited.add((curr_row, curr_col))
                for dr, dc in directions:
                    nr, nc = curr_row + dr, curr_col + dc
                    if 0 <= nr < numRows and 0 <= nc < numCols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs((i,j))
                    number_islands += 1
        return number_islands

    

        