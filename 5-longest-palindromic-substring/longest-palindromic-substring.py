class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        longest_palindrome = ""

        def getPalindrome(start, end):
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]
        
        for idx in range(n):
            # get the odd length and even length palindromes 
            odd_palindrome = getPalindrome(idx, idx)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome

            even_palindrome = getPalindrome(idx, idx+1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome

        

        