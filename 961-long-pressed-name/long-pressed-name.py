class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        npointer, tpointer = 0, 0
        while tpointer < len(typed):
            if npointer < len(name) and name[npointer] == typed[tpointer]:
                npointer += 1
                tpointer += 1
            elif tpointer > 0 and typed[tpointer] == typed[tpointer - 1]:
                tpointer += 1
            else:
                return False
        return npointer == len(name)
