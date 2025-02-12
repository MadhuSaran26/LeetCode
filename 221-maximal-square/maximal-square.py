class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        numRows, numCols = len(matrix), len(matrix[0])
        prev = curr = [0 for _ in range(numCols+1)]
        result = 0 # to store the maximum side length

        for i in range(1, numRows+1):
            for j in range(1, numCols+1):
                if matrix[i-1][j-1] == "1":
                    curr[j] = min(prev[j-1], prev[j], curr[j-1]) + 1
                    result = max(result, curr[j])
                else:
                    curr[j] = 0
            prev = curr[:]
        
        return result*result


        