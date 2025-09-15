# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for idx, llist in enumerate(lists):
            if llist:
                heappush(min_heap, (llist.val, idx, llist))
        
        dummy = ListNode()
        current = dummy

        while min_heap:
            _, idx, lnode = heappop(min_heap)
            current.next = lnode
            current = current.next
            if lnode.next:
                heappush(min_heap, (lnode.next.val, idx, lnode.next))
        
        return dummy.next
        