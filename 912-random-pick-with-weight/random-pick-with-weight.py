import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        cum_sum = 0
        for idx, num in enumerate(w):
            cum_sum += num
            self.prefix_sum[idx] = cum_sum
            

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1])
        low, high = 0, len(self.prefix_sum)-1

        while low <= high:
            mid = (low + high)//2
            if self.prefix_sum[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()