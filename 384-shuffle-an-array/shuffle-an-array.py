class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        
    def reset(self) -> List[int]:
        return self.array
        
    def shuffle(self) -> List[int]:
        #Using Fishes-Yates algorithm to swap the elements randomly to generate the random shuffle effect
        auxiliary = self.array[:]
        for idx in range(len(auxiliary)-1, -1, -1):
            swap_idx = random.randint(0, idx)
            auxiliary[idx], auxiliary[swap_idx] = auxiliary[swap_idx], auxiliary[idx]

        return auxiliary        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()