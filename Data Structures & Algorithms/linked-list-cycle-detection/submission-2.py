# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#could store every visited node in a set and detect when a node appears again. That takes O(n) extra space.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # think of it like 2 runners on a circular track the faster runner eventually catches the slower runner
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False        
        


        