# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
            
        curr, prev = head, None

        # move until left node is reached
        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left-1, right-1
        
        tail, connection = curr, prev #left node marked as tail; node before left marked as connection

        # swap nodes from left to right node
        while right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1
        
        # connect the prev node (right node) to the connection
        if connection:
            connection.next = prev
        else:
            head = prev
        # connect the tail node (left node) to the node after right
        tail.next = curr
        
        return head
        