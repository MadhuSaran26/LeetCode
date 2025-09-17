class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        flen, slen = len(firstList), len(secondList)
        fptr = sptr = 0
        result = []
        while fptr < flen and sptr < slen:
            fstart, fend = firstList[fptr]
            sstart, send = secondList[sptr]

            start = max(fstart, sstart)
            end = min(fend, send)

            if start <= end:
                result.append([start, end])

            if fend < send:
                fptr += 1
            else:
                sptr += 1
        
        return result
        