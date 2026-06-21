class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        left  = 0

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            while dq[0] < left:
                dq.popleft()
            if right - left + 1 == k:
                ans.append(nums[dq[0]])
                left += 1
        return ans                


                
                

        



        