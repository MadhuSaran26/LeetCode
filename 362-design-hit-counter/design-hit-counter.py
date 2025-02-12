class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total_count = 0  

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (self.hits[-1][0], self.hits[-1][1]+1)
        else:
            self.hits.append((timestamp, 1))
        self.total_count += 1      

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp-300:
            self.total_count -= self.hits.popleft()[1]
        return self.total_count
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)