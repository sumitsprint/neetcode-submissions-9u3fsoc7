# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        
        prev_group = tail

        while True:
            group_end = prev_group
            for _ in range(k):
                group_end = group_end.next
                if group_end is None:
                    return dummy.next

            pre = group_end.next
            tail = prev_group.next
            group_start = tail

            for _ in range(k):
                n = tail.next
                tail.next = pre
                pre = tail
                tail = n

            prev_group.next = pre


            prev_group = group_start
        return dummy.next    

















        