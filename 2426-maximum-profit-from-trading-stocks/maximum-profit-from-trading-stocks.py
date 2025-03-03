class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        # number of items (rows), remaining capacity (cols)
        dp = [[0 for _ in range(budget+1)] for _ in range(n+1)] 

        for i in range(1,n+1):
            for j in range(budget+1):
                if present[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - present[i-1]] + (future[i-1] - present[i-1]))
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][budget]    