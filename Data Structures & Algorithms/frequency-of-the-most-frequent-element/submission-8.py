class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        max_l = 0

        # grow
        for right in range(len(nums)):
            window_sum += nums[right]

            #shrink
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            #evaluate
            max_l = max(max_l, right - left + 1)

        return max_l