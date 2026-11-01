# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        pre = None

        while curr:
            n = curr.next
            curr.next = pre
            pre = curr
            curr = n

        dummy = ListNode()
        dummy.next = head

        curr = head

        new = pre

        while curr and new:
            n = curr.next
            sec = new.next
            curr.next = new
            new.next = n
            curr = n
            new = sec
        slow.next = None  
        # return dummy.next





        