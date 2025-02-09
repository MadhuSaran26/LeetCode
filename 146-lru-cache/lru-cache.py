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
        

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)
        if len(self.dict) > self.capacity:
            node2remove = self.head.next
            self._remove(node2remove)
            del self.dict[node2remove.key]
    
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)