class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        # right = len(nums) - 1
        min_l = float('inf')

        # for rightwhile left < right:
        for right in range(len(nums)):
            s += nums[right]

            while s >= target and left < len(nums):
                min_l = min(min_l, right - left + 1)
                s -= nums[left]
                left += 1
        if min_l == float('inf'):
            return 0
        return min_l            


        