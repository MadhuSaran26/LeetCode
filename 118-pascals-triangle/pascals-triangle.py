class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        prev_dp = [1] * numRows

        for i in range(numRows):
            dp = [1] * numRows
            for j in range(i+1):
                if j==0 or j==i:
                    continue
                dp[j] = prev_dp[j-1] + prev_dp[j]
            result.append(dp[:j+1])
            prev_dp = dp[:]
        
        return result

                
        
        