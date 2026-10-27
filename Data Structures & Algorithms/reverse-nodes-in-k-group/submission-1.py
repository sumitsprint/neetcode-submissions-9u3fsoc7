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

        
            for i in range(k):
                
                group_end = group_end.next
                if group_end is None:
                    return dummy.next

            group_next = group_end.next
            prev = group_next
            curr = group_prev.next
            group_start = curr

            for _ in range(k):
                n = curr.next
                curr.next = prev # reversing the link
                prev = curr # advance the pointer
                curr = n # advance the pointer

            group_prev.next = prev

            # 5. Move to the next group
            group_prev = group_start    



              

        