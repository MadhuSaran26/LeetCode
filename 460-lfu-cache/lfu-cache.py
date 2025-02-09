class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.key2node = dict() # dict that maps a key to the respective node (similar to LRU)
        self.key2freq = dict() # dict that maps a key to its respective frequency
        self.freq2nodes = dict() # dict that maps a frequency to a doubly linked list of nodes with that freq
        self.capacity = capacity
        self.min_freq = 0       

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self._updateFreq(node) # since node is accessed for reading, its frequency is updated
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key2node: # if key already exists, update node value
            node = self.key2node[key]
            node.val = value
            self._updateFreq(node) # since node is accessed for writing, its freq must be updated
        else:
            if len(self.key2node) >= self.capacity:
                self._evict() # since capacity is reached, remove the least frequently accessed node
            
            node = Node(key, value)
            self.key2node[key] = node
            self.key2freq[key] = 1
            self._addNode(node, 1) # adding new node with freq set to 1
            self.min_freq = 1 #reset min frequency to 1
        
    def _evict(self):
        head, tail = self.freq2nodes[self.min_freq]
        node2remove = head.next
        self._removeNodeFromFreqList(node2remove, self.min_freq) # removing least used node with min freq
        del self.key2freq[node2remove.key]
        del self.key2node[node2remove.key]
    
    def _removeNodeFromFreqList(self, node, freq):
        # removing node from the list which has it
        node.prev.next = node.next
        node.next.prev = node.prev

        head, tail = self.freq2nodes[freq]
        if head.next == tail: # freq list has no nodes after removal, hence deleting it
            del self.freq2nodes[freq]
    
    def _addNode(self, node, freq):
        # adding new freq to the dictionary
        if freq not in self.freq2nodes:
            head = Node(-1,-1)
            tail = Node(-1,-1)
            head.next = tail
            tail.prev = head
            self.freq2nodes[freq] = (head, tail)
        
        # adding node to the freq's corresponding DLL
        head, tail = self.freq2nodes[freq]
        prev_node = tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = tail
        tail.prev = node
    
    def _updateFreq(self, node):
        freq = self.key2freq[node.key]
        self._removeNodeFromFreqList(node, freq) # remove the node from old freq list
        self._addNode(node, freq+1) # add node to the new freq list
        self.key2freq[node.key] += 1 # updated new freq in dictionary

        if freq == self.min_freq and freq not in self.freq2nodes: # if old freq was min_freq, increment it by 1
            self.min_freq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)