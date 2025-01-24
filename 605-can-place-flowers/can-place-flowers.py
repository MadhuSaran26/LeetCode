class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if n==0:
            return True
        for idx in range(length):
            if flowerbed[idx] == 0 and (idx==0 or flowerbed[idx-1] != 1) and (idx==length-1 or flowerbed[idx+1] != 1):
                flowerbed[idx] = 1
                n -= 1
                if n==0:
                    return True
        
        return False

        