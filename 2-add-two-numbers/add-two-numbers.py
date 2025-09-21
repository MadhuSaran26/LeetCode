# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode()
        ptr3 = dummy
        while ptr1 and ptr2:
            sum_val = ptr1.val + ptr2.val + carry_over
            carry_over = sum_val // 10
            ptr3.next = ListNode(sum_val%10)
            ptr1, ptr2, ptr3 = ptr1.next, ptr2.next, ptr3.next
        
        while ptr1:
            sum_val = ptr1.val + carry_over
            carry_over = sum_val // 10
            ptr3.next = ListNode(sum_val%10)
            ptr1, ptr3 = ptr1.next, ptr3.next
        
        while ptr2:
            sum_val = ptr2.val + carry_over
            carry_over = sum_val // 10
            ptr3.next = ListNode(sum_val%10)
            ptr2, ptr3 = ptr2.next, ptr3.next
        
        if carry_over:
            ptr3.next = ListNode(carry_over)
        
        return dummy.next


        