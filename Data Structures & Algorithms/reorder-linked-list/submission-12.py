# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1st , last, 2nd, 2nd last
        
        # When the loop ends, slow points to the middle for odd-length lists and the second middle for even-length lists.
        # find the middle node 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of the linked list
        pre = None
        curr = slow.next

        while curr:
            n = curr.next
            curr.next = pre
            pre = curr
            curr = n

        # curr is head    

        # reorder the two halves alternately

        first = head
        second = pre

        while first and second:
            # first_next = first.next
            # second_next = second.next
            # first.next = second
            # first.next.next = first_next
            # second = second_next
            # first = first.next.next
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        
        slow.next = None

#forgot to advance first pointer


        
        

        
        
        






        