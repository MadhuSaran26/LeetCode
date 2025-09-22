class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_dp = [1]*n
        curr_dp = [1]*n

        for i in range(1, m):
            curr_dp = [1]*n
            for j in range(1, n):
                curr_dp[j] = prev_dp[j] + curr_dp[j-1]
            prev_dp = curr_dp[:]
        
        return curr_dp[-1]
        