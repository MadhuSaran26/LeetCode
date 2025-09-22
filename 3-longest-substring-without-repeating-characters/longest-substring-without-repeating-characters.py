class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        window = dict()
        for right in range(len(s)):
            char  = s[right]
            if char in window and window[char] >= left:
                left = window[char] + 1
            window[char] = right
            result = max(result, right - left + 1)
        return result
        