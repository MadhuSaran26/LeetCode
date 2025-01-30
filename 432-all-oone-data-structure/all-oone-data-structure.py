class AllOne:

    def __init__(self):
        self.prev_operation = 0
        self.result = ""
        self.data = dict()
        

    def inc(self, key: str) -> None:
        self.prev_operation = 0
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1
        return None

    def dec(self, key: str) -> None:
        self.prev_operation = 0
        self.data[key] -= 1
        if self.data[key] == 0:
            del self.data[key]  
        return None

    def getMaxKey(self) -> str:
        if self.prev_operation == 1:
            return self.result
        self.prev_operation = 1
        if self.data:
            count = list(self.data.values())[0]
            key = list(self.data.keys())[0]
            for key_d in self.data:
                if self.data[key_d] > count:
                    count = self.data[key_d]
                    key = key_d
            self.result = key
            return key
        else:
            self.result = ""
            return ""
        
    def getMinKey(self) -> str:
        if self.prev_operation == 2:
            return self.result
        self.prev_operation = 2
        if self.data:
            count = list(self.data.values())[0]
            key = list(self.data.keys())[0]
            for key_d in self.data:
                if self.data[key_d] < count:
                    count = self.data[key_d]
                    key = key_d
            self.result = key
            return key
        else:
            self.result = ""
            return ""
        
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()