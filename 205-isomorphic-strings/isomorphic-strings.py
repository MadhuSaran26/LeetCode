class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap = dict()
        for s_char, t_char in zip(s, t):
            if s_char in cmap and cmap[s_char] != t_char:
                return False
            if s_char not in cmap and t_char in cmap.values():
                return False
            cmap[s_char] = t_char
        return True
        