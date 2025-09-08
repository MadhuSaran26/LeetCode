import random
class Solution:

    def __init__(self, w: List[int]):
        w_sum = sum(w)
        self.weights = [num/w_sum for num in w]
        self.indices = list(range(len(w)))
        print(self.weights)
        print(self.indices)

    def pickIndex(self) -> int:
        result = random.choices(self.indices, weights=self.weights, k=1)
        return result[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()