"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = dict()
        pointer = head
        dummy = Node(-1)
        cpointer = dummy
        while pointer:
            node = Node(pointer.val)
            cpointer.next = node
            cpointer = cpointer.next
            copy_dict[pointer] = node
            pointer = pointer.next
        
        pointer = head
        cpointer = dummy.next
        while pointer:
            random_ptr = pointer.random
            if random_ptr:
                cpointer.random = copy_dict[random_ptr]
            cpointer = cpointer.next
            pointer = pointer.next
        
        return dummy.next


        