class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)
        
    def reset(self) -> List[int]:
        self.array = list(self.original)
        return self.array
        
    def shuffle(self) -> List[int]:
        #Using Fishes-Yates algorithm to swap the elements randomly to generate the random shuffle effect
        for idx in range(len(self.array)):
            swap_idx = random.randrange(len(self.array))
            self.array[idx], self.array[swap_idx] = self.array[swap_idx], self.array[idx]

        return self.array        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()