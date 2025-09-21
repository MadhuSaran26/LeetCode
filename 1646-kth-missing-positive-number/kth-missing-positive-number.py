class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        aptr = 0
        while i <= arr[-1]:
            if arr[aptr] == i:
                aptr += 1
            else:
                k -= 1
            if k == 0:
                return i
            i += 1
        return i + k -1
        


        