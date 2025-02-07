class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # dp to hold the longest subsequence length until i
        dp = [1]*n
        
        for i in range(1,n):
            #checking all indexes before i
            for j in range(i):
                if nums[i] > nums[j]:
                    #get the maximum len considering subseq ending at j
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        