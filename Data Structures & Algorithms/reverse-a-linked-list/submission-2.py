# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            #head
            # 0, 1, 2, 3, None  
            #None, 0, 1, 2, 3
            next_node = curr.next # save the next refrence (1)
            curr.next = prev #  1 -> None | 0 -> None
            prev = curr # None -> 0
            curr = next_node #0  -> 1 eventually None
        return prev    

        
        