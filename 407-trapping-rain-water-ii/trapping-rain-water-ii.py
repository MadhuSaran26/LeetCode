class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        numRows, numCols = len(heightMap), len(heightMap[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)] #up, right, down , left
        result = 0
        heap = []
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]

        # adding left and right edge cells to the heap
        for i in range(numRows):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][numCols-1], i, numCols-1))
            visited[i][0] = visited[i][numCols-1] =True
        
        # adding top and bottom edge cells to the heap
        for j in range(numCols):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[numRows-1][j], numRows-1, j))
            visited[0][j] = visited[numRows-1][j] = True
        
        while heap:
            height, row, col = heappop(heap)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < numRows and 0 <= nc < numCols and not visited[nr][nc]:
                    result += max(0, height - heightMap[nr][nc])
                    heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
                    visited[nr][nc] = True
        
        return result





        