class AllOne:

    def __init__(self):
        self.prev_op = 0
        self.data = dict()
        self.result = ''

    def inc(self, key: str) -> None:
        self.prev_op = 0
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def dec(self, key: str) -> None:
        self.prev_op = 0
        self.data[key] -= 1
        if self.data[key] == 0:
            del self.data[key]
        

    def getMaxKey(self) -> str:  
        if self.prev_op == 1:
            return self.result
        self.prev_op = 1
        if self.data:
            value = list(self.data.values())[0]
            max_key = list(self.data.keys())[0]
            for key in self.data:
                if self.data[key] > value:
                    value = self.data[key]
                    max_key = key
            self.result = max_key
            return max_key
        else:
            self.result = ''
            return '' 

    def getMinKey(self) -> str: 
        if self.prev_op == 2:
            return self.result
        self.prev_op = 2
        if self.data:
            value = list(self.data.values())[0]
            min_key = list(self.data.keys())[0]
            for key in self.data:
                if self.data[key] < value:
                    value = self.data[key]
                    min_key = key
            self.result = min_key
            return min_key
        else:
            self.result = ''
            return ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()