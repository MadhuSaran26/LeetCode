class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<high:
            mid = (low+high)//2
            hours_spent = 0

            for num in piles:
                hours_spent += math.ceil(num/mid)
            
            if hours_spent <= h:
                high = mid
            else:
                low = mid+1

        return high



        