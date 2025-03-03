class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        numRows, numCols = len(maze), len(maze[0])
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque([start])
        visited[start[0]][start[1]] == True

        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            for dr, dc in directions:
                nr, nc = curr[0], curr[1]
                # move the ball in chosen direction until it can
                while 0 <= nr < numRows and 0 <= nc < numCols and maze[nr][nc]==0:
                    nr += dr
                    nc += dc
                # Revert the last move to get the cell where the ball stops rolling
                nr -= dr
                nc -= dc
                if not visited[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc]=True
        
        return False
                