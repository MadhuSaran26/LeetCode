class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        if len(set(s)) != len(set(t)):
            return False
        cmap = dict()
        # since order is preserved, the order of characters in t can be used to check the cmap consistency
        for i, char in enumerate(s):
            if char in cmap and cmap[char] != t[i]:
                return False
            cmap[char] = t[i]
        return True
        