class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        mi = float('inf')
        for right in range(len(nums)):
            s += nums[right]

            while s >= target:
                s -= nums[left]
                mi = min(mi, right -left + 1)
                left += 1

        if mi == float('inf'):
            return 0
                    
        return mi        






        