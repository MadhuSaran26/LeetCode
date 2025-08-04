from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        s1_count = Counter(s1)
        window_count = defaultdict(int)
        left = 0
        for right in range(len_s2):
            window_count[s2[right]] += 1
            if right - left + 1 == len_s1:
                print(window_count)
                print(s1_count)
                if window_count == s1_count:
                    return True
                window_count[s2[left]] -= 1
                if not window_count[s2[left]]:
                    del window_count[s2[left]]
                left += 1
        return False


        