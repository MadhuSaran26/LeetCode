class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        npointer = tpointer = 0
        nlen, tlen = len(name), len(typed)
        ncntr, tcntr = Counter(name), Counter(typed)
        if len(ncntr) != len(tcntr):
            return False
        for char in ncntr:
            if ncntr[char] > tcntr[char]:
                return False
        while npointer < nlen and tpointer < tlen:
            if name[npointer] != typed[tpointer]:
                return False
            else:
                char = name[npointer]
                while npointer < nlen and tpointer < tlen and name[npointer] == typed[tpointer] and name[npointer] == char:
                    npointer += 1
                    tpointer += 1
                if npointer < nlen and name[npointer] != char:
                    while tpointer < tlen and typed[tpointer] == char:
                        tpointer += 1
                elif npointer == nlen and tpointer < tlen and typed[tpointer] == char:
                    while tpointer < tlen and typed[tpointer] == char:
                        tpointer += 1
                elif npointer < nlen:
                    return False
        return npointer == nlen and tpointer == tlen