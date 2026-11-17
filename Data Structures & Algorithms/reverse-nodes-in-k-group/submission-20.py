# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
    

        while True:
            group_end = prev_group            
            for _ in range(k):
                group_end = group_end.next
                if group_end is None:
                    return dummy.next

            curr = prev_group.next
            pre = group_end.next
            group_start = curr

            for _ in range(k):
                n = curr.next
                curr.next = pre
                pre = curr
                curr = n

            prev_group.next = pre
            prev_group = group_start
            








            





                



        