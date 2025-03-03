class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            if i==n:
                return 1
            if s[i]=="0":
                return 0
            
            ways = helper(i+1)

            if i != n-1 and s[i:i+2] <= "26":
                ways += helper(i+2)
            
            memo[i] = ways
            return ways
        
        return helper(0)
