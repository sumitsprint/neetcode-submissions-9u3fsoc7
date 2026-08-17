class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        min_length = float('inf')

        for right in range(len(nums)):
            n = nums[right]
            s += n

            while s >= target and left < len(nums):
                min_length = min(min_length, right - left + 1)
                s -= nums[left]
                left += 1
                


        if min_length == float('inf'):
            return 0        
        return min_length 
        