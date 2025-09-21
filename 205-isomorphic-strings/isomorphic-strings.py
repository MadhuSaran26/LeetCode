class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cmap = dict()
        # since order is preserved, the order of characters in t can be used to check the cmap consistency
        for s_char, t_char in zip(s, t):
            if s_char in cmap and cmap[s_char] != t_char:
                return False
            if s_char not in cmap and t_char in cmap.values():
                return False
            cmap[s_char] = t_char
        return True
        