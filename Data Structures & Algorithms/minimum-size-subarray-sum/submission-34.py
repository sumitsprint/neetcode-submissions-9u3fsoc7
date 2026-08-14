class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        s = 0
        left = 0

        for i in range(len(nums)):
            s += nums[i]

            while s >= target:
                min_l = min(min_l, i -left + 1)
                s -= nums[left]
                left += 1
        if min_l == float('inf'):
            return 0    
        return min_l        
        
                
        