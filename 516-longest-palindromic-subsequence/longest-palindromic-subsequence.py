class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(None)
        def recursive(l, r):
            if l == r:
                return 1
            if l > r:
                return 0
            if s[l] == s[r]:
                answer = recursive(l+1, r-1) + 2
            else:
                answer = max(recursive(l+1, r), recursive(l, r-1))
            return answer
        
        return recursive(0, len(s)-1)