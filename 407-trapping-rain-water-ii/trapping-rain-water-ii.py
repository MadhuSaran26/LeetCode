class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        numRows, numCols = len(heightMap), len(heightMap[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)] #up, right, down , left
        result = 0
        heap = []
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]

        # adding left and right edge cells to the heap
        for i in range(numRows):
            for j in [0, numCols-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        # adding top and bottom edge cells to the heap
        for j in range(numCols):
            for i in [0, numRows-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        while heap:
            height, row, col = heappop(heap)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < numRows and 0 <= nc < numCols and not visited[nr][nc]:
                    result += max(0, height - heightMap[nr][nc])
                    heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
                    visited[nr][nc] = True
        
        return result





        