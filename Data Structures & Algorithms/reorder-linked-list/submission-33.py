# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        

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

        seo = pre
        first = head
        while first and seo:
            first_next = first.next
            second_next = seo.next
            first.next = seo
            seo.next = first_next
            first = first_next
            seo = second_next    

        slow.next = None    



        