class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        heap = []
        for interval in intervals:
            if heap and heap[0] < interval[0]:
                heappop(heap)
            heappush(heap, interval[1])
        return len(heap)


        