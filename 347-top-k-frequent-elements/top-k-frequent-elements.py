from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        count_heap = [(-count, num) for num, count in nums_count.items()]
        heapify(count_heap)
        result = []
        while k > 0:
            _, num = heappop(count_heap)
            k -= 1
            result.append(num)
        return result