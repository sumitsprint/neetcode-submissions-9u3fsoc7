class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        min_length = float('inf')



        for right in range(len(nums)):
            s += nums[right]

            while s >= target and left < len(nums):
                length = right - left + 1
                min_length = min(length, min_length)
                s -= nums[left]
                left += 1
                
        if min_length == float('inf'):
            return 0        
        return min_length        




                 


        