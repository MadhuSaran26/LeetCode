from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_length = max_freq = 0
        window = defaultdict(int)
        
        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while max_freq + k < right - left + 1:
                window[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length



        