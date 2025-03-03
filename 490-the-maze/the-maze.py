class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        numRows, numCols = len(maze), len(maze[0])
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited[start[0]][start[1]] == True
        start, destination = tuple(start), tuple(destination)
        queue = deque([start])

        while queue:
            crow, ccol = queue.popleft()
            if (crow, ccol) == destination:
                return True
            for dr, dc in directions:
                nr, nc = crow, ccol
                # move the ball in chosen direction until it can
                while 0 <= nr < numRows and 0 <= nc < numCols and maze[nr][nc]==0:
                    nr += dr
                    nc += dc
                # Revert the last move to get the cell where the ball stops rolling
                nr -= dr
                nc -= dc
                if not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc]=True
        
        return False
                