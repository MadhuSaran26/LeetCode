# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode()
        ptr3 = dummy
        while ptr1 or ptr2 or carry:
            sum_val = carry
            if ptr1:
                sum_val += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                sum_val += ptr2.val
                ptr2 = ptr2.next
            carry = sum_val // 10
            ptr3.next = ListNode(sum_val%10)
            ptr3 = ptr3.next
        
        return dummy.next


        