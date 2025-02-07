class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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