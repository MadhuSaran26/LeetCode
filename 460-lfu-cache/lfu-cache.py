class LFUCache:

    def __init__(self, capacity: int):
        self.key2val = dict() # maps a key to its value
        self.key2freq = dict() # maps a key to its freq
        self.freq2keys = defaultdict(OrderedDict) # maps freq to a OrderdedDict of keys with insertion order
        self.capacity = capacity
        self.min_freq = 0     

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self._updateFreq(key) # update freq, as the key is accessed
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        
        if key in self.key2val:
            self.key2val[key] = value # if key already exists, update value
            self._updateFreq(key) # update freq, as the key is accessed
        else:
            if len(self.key2val) >= self.capacity:
                self._evict() # evict least frequently used key
            
            self.key2val[key] = value
            self.key2freq[key] = 1
            self.freq2keys[1][key] = 1 # Insert new key to freq 1
            self.min_freq = 1 # Reset min_freq to 1
    
    def _evict(self):
        # pop least recently used from the dict of least freq values
        del_key, _ = self.freq2keys[self.min_freq].popitem(last=False) # pops first added item
        del self.key2val[del_key]
        del self.key2freq[del_key]
    
    def _updateFreq(self, key):
        freq = self.key2freq[key] # old freq
        self.key2freq[key] = freq + 1
        self.freq2keys[freq].pop(key) # Remove key from old freq dict
        if not self.freq2keys[freq]: # if old freq dict is empty after removal, delete it
            del self.freq2keys[freq]
        self.freq2keys[freq+1][key] = 1 # add key to new freq

        if self.min_freq not in self.freq2keys: # if min_freq not in freq2keys, increment min_freq by 1
            self.min_freq += 1



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)