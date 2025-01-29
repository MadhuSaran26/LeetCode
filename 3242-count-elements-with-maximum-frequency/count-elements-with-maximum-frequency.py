class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq_cnt = Counter(count.values())
        max_freq = max(list(freq_cnt.keys()))
        return max_freq * freq_cnt[max_freq]




        