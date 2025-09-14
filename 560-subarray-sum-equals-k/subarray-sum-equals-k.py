from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = sum_idx = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 # Make sure that subarrays starting from index 0 that sum to k are counted.

        for num in nums:
            sum_idx += num
            if sum_idx - k in prefix_count:
                result += prefix_count[sum_idx - k]
            prefix_count[sum_idx] += 1
        
        return result

        



        