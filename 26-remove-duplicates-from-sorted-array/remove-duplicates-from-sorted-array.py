class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastUnique = 0
        visited = set()

        for idx in range(len(nums)):
            if nums[idx] not in visited:
                visited.add(nums[idx])
                nums[idx], nums[lastUnique] = nums[lastUnique], nums[idx]
                lastUnique += 1
        
        return lastUnique
        