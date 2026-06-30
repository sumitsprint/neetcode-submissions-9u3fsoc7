class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        left = 0
        ans = []
        for right in range(n):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()
                # left += 1

            if right - left + 1 == k:
                ans.append(nums[dq[0]])
                left += 1
        return ans            


        
        

        