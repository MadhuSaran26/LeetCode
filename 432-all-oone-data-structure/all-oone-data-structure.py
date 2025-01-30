class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.data = dict()
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.data:
            freq_node = self.data[key]
            freq = freq_node.freq
            freq_node.keys.remove(key)
        else:
            freq = 0
            freq_node = self.head
        
        next_node = freq_node.next
        if next_node.freq != freq+1:
            new_node = Node(freq+1)
            new_node.keys.add(key)
            new_node.prev = freq_node
            new_node.next = next_node
            next_node.prev = new_node
            freq_node.next = new_node 
            self.data[key] = new_node
        else:
            next_node.keys.add(key)
            self.data[key] = next_node
        
        if freq_node != self.head and not freq_node.keys:
            self.removeNode(freq_node)
            del freq_node
        
        return None

    def dec(self, key: str) -> None:
        freq_node = self.data[key]
        freq_node.keys.remove(key)
        freq = freq_node.freq - 1

        prev_node = freq_node.prev
        if freq == 0:
            del self.data[key]
        elif prev_node.freq != freq:
            new_node = Node(freq)
            new_node.keys.add(key)
            new_node.prev = prev_node
            new_node.next = freq_node
            prev_node.next = new_node
            freq_node.prev = new_node
            self.data[key] = new_node
        else:
            prev_node.keys.add(key)
            self.data[key] = prev_node
          
        if not freq_node.keys:
            self.removeNode(freq_node)
            del freq_node

        return None 

    def getMaxKey(self) -> str:  
        if self.tail.prev == self.head:
            return '' 
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str: 
        if self.head.next == self.tail:
            return ''
        return next(iter(self.head.next.keys))
    
    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()