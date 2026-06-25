class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # candidate indices
        ans = []
        left = 0

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Remove indices that are outside the window
            if dq[0] < left:
                dq.popleft()

            # Window of size k has been formed
            if right - left + 1 == k:

                # Front index stores the maximum
                ans.append(nums[dq[0]])

                # Slide the window
                left += 1

        return ans
        

        
        