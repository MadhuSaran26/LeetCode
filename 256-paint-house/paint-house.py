class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        numRows, numCols = len(costs), len(costs[0])
        dp = [[float('inf') for _ in range(numCols)] for _ in range(numRows)]
        dp[0] = costs[0]
        for i in range(1, numRows):
            heap = [(elem, idx) for idx, elem in enumerate(dp[i-1])]
            heapify(heap)
            for j in range(numCols):
                if heap[0][1] != j:
                    dp[i][j] = costs[i][j] + heap[0][0]
                else:
                    temp_tup = heappop(heap)
                    dp[i][j] = costs[i][j] + heap[0][0]
                    heappush(heap, temp_tup)
        
        return min(dp[numRows-1])