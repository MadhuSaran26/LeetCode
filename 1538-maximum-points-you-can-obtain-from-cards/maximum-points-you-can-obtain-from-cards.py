class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        wsize = len(cardPoints) - k
        left = 0
        window_sum = min_sum = sum(cardPoints[:wsize])
        for right in range(wsize, len(cardPoints)):
            window_sum += cardPoints[right]
            window_sum -= cardPoints[left]
            min_sum = min(min_sum, window_sum)
            left += 1
        return total - min_sum