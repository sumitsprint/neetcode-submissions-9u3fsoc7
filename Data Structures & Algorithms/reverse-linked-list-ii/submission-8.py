# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        before = dummy # points to node 1
        curr = before.next # curr and end Both point to node 2 

        end = curr #end pointer is important: it remembers node 2, which will become the tail of the reversed section
        pre = None
        for _ in range(left - 1):
            before = before.next

        curr = before.next
        end = curr

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        before.next = pre  # Connect node before the section to the new head
        end.next = curr     # Connect the reversed section's tail to the remaining list
        return dummy.next   # Return the head of the complete list    
        
            






