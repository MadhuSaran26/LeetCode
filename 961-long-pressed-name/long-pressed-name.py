class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        npointer = tpointer = 0
        nlen, tlen = len(name), len(typed)
        while tpointer < tlen:
            if npointer < nlen and name[npointer] == typed[tpointer]:
                npointer += 1
                tpointer += 1
                if  0 < npointer < nlen and tpointer < tlen and name[npointer] == name[npointer-1] and name[npointer] == typed[tpointer]:
                    continue
                while 0 < tpointer < tlen and typed[tpointer] == typed[tpointer-1]:
                    tpointer += 1
            else:
                return False

        return npointer == nlen