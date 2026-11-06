class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # the faster runner eventually catches the slower runner

        # Find the meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = nums[0]

        while not slow == fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


        #the variables store values that become the next indices.