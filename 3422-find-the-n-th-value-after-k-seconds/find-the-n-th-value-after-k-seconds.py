class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9+7
        arr = [1]*n
        for _ in range(k):
            for idx in range(1, n):
                arr[idx] += arr[idx-1]
                #arr[idx] %= MOD
        
        return arr[n-1] % MOD
        