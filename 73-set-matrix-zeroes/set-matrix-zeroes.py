class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        numRows, numCols = len(matrix), len(matrix[0])
        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for row in zero_rows:
            matrix[row] = [0] * numCols
        
        for col in zero_cols:
            for i in range(numRows):
                matrix[i][col] = 0
        

        