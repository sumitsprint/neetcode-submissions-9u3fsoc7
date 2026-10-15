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

        curr = before.next
        pre = None
        end = curr

        for _ in range(right - left + 1):
            n = curr.next
            curr.next = pre
            pre = curr
            curr = n

        before.next = pre 
        end.next = curr
        return dummy.next





        
        




        