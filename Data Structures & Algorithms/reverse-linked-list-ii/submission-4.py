# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Dummy node handles the case where left = 1
        dummy = ListNode(0, head)
        before = dummy

        # Move 'before' to the node just before position left
        for _ in range(left - 1):
            before = before.next

        # curr starts at the first node to be reversed
        curr = before.next

        # Save the original first node; it becomes the tail after reversal
        end = curr

        # Build the reversed section
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next       # Save the next node
            curr.next = prev      # Reverse the current link
            prev = curr           # Move prev forward
            curr = nxt            # Move curr forward

        # Connect the node before the section to the new head
        before.next = prev

        # Connect the new tail to the node after the section
        end.next = curr

        # Return the list's head (handles left = 1 too)
        return dummy.next
