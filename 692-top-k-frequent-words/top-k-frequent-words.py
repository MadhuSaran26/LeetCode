class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        heap = [(-cnt, word) for word, cnt in count.items()]
        heapify(heap)
        result = []
        for _ in range(k):
            _, word = heappop(heap)
            result.append(word)
        return result

        