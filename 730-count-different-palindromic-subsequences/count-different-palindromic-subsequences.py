class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1000000007
        n = len(s)
        # 4 possible unique characters in a string - a, b, c, d
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
        
        for i in range(n-1, -1, -1):
            # single character indexes are not set to 1 yet. So, j will range from i to n
            for j in range(i, n):
                # need to check all four characters
                for k in range(4):
                    char = chr(ord('a') + k)
                    if i == j:
                        # set single character index, if s[i] corresponds to considered character
                        if s[i] == char:
                            dp[k][i][j] = 1
                        else:
                            dp[k][i][j] = 0
                    # for j > i
                    else:
                        #skip that index if it doesn't match the considered character
                        if s[i] != char:
                            dp[k][i][j] = dp[k][i+1][j]
                        elif s[j] != char:
                            dp[k][i][j] = dp[k][i][j-1]
                        # when both characters match the considered character
                        else:
                            # no other character in between two considered indexes
                            if j == i+1:
                                # palindromes of length 1 and 2 - a, aa
                                dp[k][i][j] = 2
                            else:
                                # palindrome length > 2
                                dp[k][i][j] = 2
                                # count all palindromes of a, b, c, d within the sub-window s[i+1][j-1]
                                for m in range(4):
                                    dp[k][i][j] += dp[m][i+1][j-1]
                                    dp[k][i][j] %= MOD
        
        result = 0
        for m in range(4):
            result += dp[m][0][n-1]
            result %= MOD
        
        return result

