class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head # connect the node with head
        group_prev = dummy # previous group

        while True:
            group_end = group_prev # start from previous  group end
            for i in range(k):
                group_end = group_end.next
                if group_end is None:
                    return dummy.next  # we got the group 
                    # we don't reverse it. we return head

            group_next = group_end.next # store the next group start node
            prev = group_next # pointers for reversal
            # prev = group_end.next
            curr = group_prev.next # pointer for reversal
            group_start = curr

            # reversing the group
            for _ in range(k):
                n = curr.next
                curr.next = prev # reversing the link
                prev = curr # advance the pointer
                curr = n # advance the pointer


            group_prev.next = prev # connecting the previous group to reversed group
            # 5. Move to the next group
            group_prev = group_start    



              

        