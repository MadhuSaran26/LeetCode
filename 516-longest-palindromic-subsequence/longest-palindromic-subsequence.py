class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #Iterative approach - 1D DP
        n = len(s)
        curr, prev = [0]*n, [0]*n
        for i in range(n-1, -1, -1):
            curr[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    curr[j] = prev[j-1] + 2
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return curr[n-1]

        ##Iterative approach - 2D DP
        #n = len(s)
        #dp = [[0 for _ in range(n)] for _ in range(n)]
        #for i in range(n-1, -1, -1):
        #    dp[i][i] = 1
        #    for j in range(i+1, n):
        #        if s[i] == s[j]:
        #            dp[i][j] = dp[i+1][j-1] + 2
        #        else:
        #            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #return dp[0][n-1]

        ##Recursive approach
        #@lru_cache(None)
        #def recursive(l, r):
        #    if l == r:
        #        return 1
        #    if l > r:
        #        return 0
        #    if s[l] == s[r]:
        #        answer = recursive(l+1, r-1) + 2
        #    else:
        #        answer = max(recursive(l+1, r), recursive(l, r-1))
        #    return answer
        #
        #return recursive(0, len(s)-1)