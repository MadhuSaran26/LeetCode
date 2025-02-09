class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = dict()
        self.capacity = capacity
        self.count = 0
        

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.count -= 1
        node = Node(key, value)
        self.dict[key] = node
        self.add(node)
        self.count += 1
        if self.count == self.capacity+1:
            node2remove = self.head.next
            self.remove(node2remove)
            del self.dict[node2remove.key]
            self.count -= 1
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)