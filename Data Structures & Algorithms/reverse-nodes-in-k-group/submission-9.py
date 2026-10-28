# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        group_prev = dummy

        while True:
            group_end = group_prev
            

            for _ in range(k):
                group_end = group_end.next
                if group_end is None:
                    return dummy.next

            group_start = group_prev.next
            curr = group_prev.next
            prev = group_end.next
            # group_next = group_end.next

            for _ in range(k):
                n = curr.next
                curr.next = prev
                prev  = curr
                curr = n

            
            group_prev.next = prev
            group_prev = group_start
            








        
                