from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tcnt = Counter(t)
        have, need = 0, len(tcnt)
        window_cnt = defaultdict(int)
        min_window = [float('inf'), -1, -1]
        for right in range(len(s)):
            window_cnt[s[right]] += 1
            if s[right] in tcnt and window_cnt[s[right]] == tcnt[s[right]]:
                have += 1
            
            while have == need:
                if min_window[0] > right - left + 1:
                    min_window = [right - left + 1, left, right]
                
                window_cnt[s[left]] -= 1
                if s[left] in tcnt and window_cnt[s[left]] < tcnt[s[left]]:
                    have -= 1
                left += 1
        
        return s[min_window[1]:min_window[2]+1] if min_window[0] != float('inf') else ''



        