class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)        

        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1   

        node = self.node_map[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.node_map:
            self._remove(self.node_map[key])
        
        node = ListNode(key, value)
        self.node_map[key] = node
        self._add(node)

        if len(self.node_map) > self.capacity:
            node_to_del = self.head.next
            self._remove(node_to_del)

            del self.node_map[node_to_del.key]
        
            
    
    def _add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)