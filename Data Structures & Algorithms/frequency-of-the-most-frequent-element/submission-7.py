class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        w_s = 0
        max_l = 0

        for right in range(len(nums)):
            w_s += nums[right]

            while nums[right] * (right -left + 1) - w_s > k:
                w_s -= nums[left]
                left += 1
            max_l = max(max_l, right -left + 1)
        return max_l
