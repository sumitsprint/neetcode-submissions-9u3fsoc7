# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        pn = tail

        for _ in range(left - 1):
            pn = pn.next

        curr = pn.next
        end = curr
        pre = None

        for _ in range(right - left + 1):
            n = curr.next
            curr.next = pre
            pre = curr
            curr = n

        pn.next = pre
        end.next = curr

        

        return dummy.next    





        