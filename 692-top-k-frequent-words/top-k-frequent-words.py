from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-cnt, word) for word, cnt in count.items()]
        heapify(heap)
        result = []
        for _ in range(k):
            result.append(heappop(heap)[1])
        return result

        