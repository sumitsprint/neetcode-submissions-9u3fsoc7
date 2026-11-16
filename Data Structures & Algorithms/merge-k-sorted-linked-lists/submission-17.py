# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        dummy = ListNode()
        tail = dummy
        while h:
            value, i, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next

            if tail.next:
                node = tail.next
                heapq.heappush(h, (node.val, i, node))
        tail.next = None
        return dummy.next        



            

        