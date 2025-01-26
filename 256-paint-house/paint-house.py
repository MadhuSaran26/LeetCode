class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        numRows, numCols = len(costs), len(costs[0])
        for i in range(1, numRows):
            heap = [(elem, idx) for idx, elem in enumerate(costs[i-1])]
            heapify(heap)
            for j in range(numCols):
                if heap[0][1] != j:
                    costs[i][j] = costs[i][j] + heap[0][0]
                else:
                    temp_tup = heappop(heap)
                    costs[i][j] = costs[i][j] + heap[0][0]
                    heappush(heap, temp_tup)
        
        return min(costs[numRows-1])