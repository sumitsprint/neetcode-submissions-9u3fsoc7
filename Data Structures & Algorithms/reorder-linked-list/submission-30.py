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

        first = head
        second = pre 

        while second:
            first_second = first.next 
            second_sec  = second.next 
            first.next = second
            second.next = first_second
            first = first_second
            second = second_sec

        slow.next = None
        


          






        