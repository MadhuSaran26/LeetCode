class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for idx in range(len(nums)):
            while queue and nums[queue[-1]] < nums[idx]:
                queue.pop()
            if queue and queue[0]+k == idx:
                queue.popleft()
            queue.append(idx)
            if idx+1 >= k:
                result.append(nums[queue[0]])
        
        return result