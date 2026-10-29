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

        curr = head
        new_head = pre

        while new_head:
            n = curr.next
            n_n = new_head.next
            curr.next = new_head
            new_head.next = n
            curr = n
            new_head = n_n
        slow.next = None    








            


        
        