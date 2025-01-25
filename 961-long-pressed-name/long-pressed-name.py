class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        npointer = tpointer = 0
        nlen, tlen = len(name), len(typed)
        while tpointer < tlen:
            if npointer < nlen and name[npointer] == typed[tpointer]:
                npointer += 1
                tpointer += 1
            elif tpointer > 0 and typed[tpointer] == typed[tpointer-1]:
                tpointer += 1
            else:
                return False

        return npointer == nlen