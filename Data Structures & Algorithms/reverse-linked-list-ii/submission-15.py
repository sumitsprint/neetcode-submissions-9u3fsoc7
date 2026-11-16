# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy 

        for _ in range(left - 1):
            before = before.next

        group_end = before

        for _ in range(right - left + 1):
            group_end = group_end.next

        curr = before.next
        pre = group_end.next

        for _ in range(right - left + 1):
            n = curr.next
            curr.next  = pre
            pre = curr
            curr = n  

        before.next = pre
        return dummy.next


