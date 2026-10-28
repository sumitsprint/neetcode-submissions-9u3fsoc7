# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        while h:
            value, i, node = heapq.heappop(h)

            curr.next = node

            curr = curr.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        curr.next = None        
        return dummy.next        




                    
        