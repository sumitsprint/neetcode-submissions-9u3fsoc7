class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        min_length = float('inf')

        for i in range(len(nums)):
            s += nums[i]

            while s >= target:
                min_length = min(min_length, (i-left+1))
                s = s- nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length    
            
                   
                
                
            
            
        
        
        