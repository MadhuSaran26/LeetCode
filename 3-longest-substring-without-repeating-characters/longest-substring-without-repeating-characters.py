class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        window = set()
        for right in range(len(s)):
            char  = s[right]
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            result = max(result, right - left + 1)
        return result
        