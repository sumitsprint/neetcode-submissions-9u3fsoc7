# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half

        curr = slow.next

        pre = None

        while curr:
            n = curr.next
            curr.next = pre
            pre = curr
            curr = n


        #reorderList
        first = head
        second = pre

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next
            first = first_next
            second = second_next

        slow.next = None    
            



        

        