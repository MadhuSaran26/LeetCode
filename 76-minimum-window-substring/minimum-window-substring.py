class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        s = list(s)
        slen = len(s)
        tcnt = Counter(t)
        min_window = (float('inf'), -1, -1)
        window_cnt = defaultdict(int)
        result = []
        have, need = 0, len(tcnt)
        for right in range(slen):
            window_cnt[s[right]] += 1
            if s[right] in tcnt and window_cnt[s[right]] == tcnt[s[right]]:
                have += 1
            while have == need:
                if min_window[0] > right-left+1:
                    min_window = (right-left+1, left, right)
               
                window_cnt[s[left]] -= 1
                if s[left] in tcnt and window_cnt[s[left]] < tcnt[s[left]]:
                    have -= 1
                left += 1

        return ''.join(s[min_window[1]:min_window[2]+1]) if min_window[0] != float('inf') else ''



        