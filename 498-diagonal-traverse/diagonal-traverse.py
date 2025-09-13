class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_right = True
        numRows, numCols = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        for _ in range(numRows * numCols):
            result.append(mat[row][col])
            if up_right:
                if col == numCols - 1:
                    row += 1
                    up_right = False
                elif row == 0:
                    col += 1
                    up_right = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == numRows - 1:
                    col += 1
                    up_right = True
                elif col == 0:
                    row += 1
                    up_right = True
                else:
                    row += 1
                    col -= 1
        
        return result



        