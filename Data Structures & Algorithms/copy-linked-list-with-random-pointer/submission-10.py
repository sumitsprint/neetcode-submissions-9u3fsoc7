"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        curr = head

        # Step 1: Create a copy of every node
        # When you use curr as a dictionary key, Python identifies that node object as a whole. It doesn't automatically follow its next or random pointers.
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect the copied nodes
        
        curr = head

        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        # Step 3: Return the head of the copied list
        return copies.get(head)    



          









        