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

        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left-1, right-1
        
        tail, connection = curr, prev

        while right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1

        if connection:
            connection.next = prev
        else:
            head = prev
        tail.next = curr
        
        return head
        