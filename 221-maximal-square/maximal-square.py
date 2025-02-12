class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        numRows, numCols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(numCols+1)] for _ in range(numRows+1)]
        result = 0 # to store the maximum side length

        for i in range(1, numRows+1):
            for j in range(1, numCols+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    result = max(result, dp[i][j])
        
        return result*result


        