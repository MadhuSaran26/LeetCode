class LFUCache:

    def __init__(self, capacity: int):
        self.key2val = dict()
        self.key2freq = dict()
        self.freq2keys = defaultdict(OrderedDict)
        self.capacity = capacity
        self.min_freq = 0     

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self._updateFreq(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        
        if key in self.key2val:
            self.key2val[key] = value
            self._updateFreq(key)
            return None
        
        else:
            if len(self.key2val) >= self.capacity:
                self._evict()
            
            self.key2val[key] = value
            self.key2freq[key] = 1
            self.freq2keys[1][key] = 1
            self.min_freq = 1
    
    def _evict(self):
        # pop least recently used from the dict of least freq values
        del_key, _ = self.freq2keys[self.min_freq].popitem(last=False) 
        del self.key2val[del_key]
        del self.key2freq[del_key]
    
    def _updateFreq(self, key):
        freq = self.key2freq[key]
        self.key2freq[key] = freq + 1
        self.freq2keys[freq].pop(key)
        if not self.freq2keys[freq]:
            del self.freq2keys[freq]
        self.freq2keys[freq+1][key] = 1

        if self.min_freq not in self.freq2keys:
            self.min_freq += 1



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)