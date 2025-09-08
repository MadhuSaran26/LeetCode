class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                s_left = s[left+1 : right+1] # skip s[left]
                s_right = s[left : right] # skip s[right]
                return s_left == s_left[::-1] or s_right == s_right[::-1]
            left += 1
            right -= 1
        return True

        