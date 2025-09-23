class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(current, start):
            result.append(current[:])
            for i in range(start, n):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()
        backtrack([], 0)
        return result
        