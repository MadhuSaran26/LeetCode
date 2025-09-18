class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        tcount = Counter(t)
        have, need = 0, len(tcount)
        window = defaultdict(int)
        left = 0
        min_length = [float('inf'), -1, -1]
        for right, char in enumerate(s):
            window[char] += 1
            if window[char] == tcount[char]:
                have += 1
            while have == need:
                if min_length[0] > right - left + 1:
                    min_length = [right - left + 1, left, right]
                window[s[left]] -= 1
                if s[left] in tcount and window[s[left]] < tcount[s[left]]:
                    have -= 1
                left += 1
            
        
        return s[min_length[1]:min_length[2]+1] if min_length != float('inf') else ""

            

        