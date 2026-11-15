# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        tail = dummy
        while h:
            
            value, i, node = heapq.heappop(h)     
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        tail.next = None        
        return dummy.next        


               



        