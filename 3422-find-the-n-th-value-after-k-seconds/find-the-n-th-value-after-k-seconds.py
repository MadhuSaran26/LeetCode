class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9+7
        arr = [1]*n
        for _ in range(k):
            prefix_sum = []
            curr_sum = 0
            for num in arr:
                curr_sum += num
                prefix_sum.append(curr_sum)
            arr = prefix_sum
        
        return arr[n-1] % MOD
        