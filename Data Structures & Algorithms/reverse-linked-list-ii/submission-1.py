# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        pos = 1

        while pos < left:
            curr = curr.next
            pos += 1
        

        dummy = ListNode(0, head)
        before  = dummy

        for _ in range(left- 1):
            before = before.next

        curr = before.next    
        prev = None
        end = curr

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        before.next = prev
        end.next  = curr

        return dummy.next    


       




        
        
        
        