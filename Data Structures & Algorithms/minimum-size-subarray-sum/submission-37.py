class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ms = float('inf')
        left = 0
        s = 0
        
        for right in range(len(nums)):
            
            s += nums[right]
            while s >= target:
                ms = min(ms, right-left+1)
                
                s -= nums[left]
                left += 1
        if ms == float('inf'):
            return  0       
                

        return ms        






            

          














        