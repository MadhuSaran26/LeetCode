class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def countPalindrome(start, end):
            count = 0
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            return count
        
        for i in range(len(s)):
            result += countPalindrome(i, i)
            if i < len(s) - 1:
                result += countPalindrome(i, i+1)
        
        return result

        