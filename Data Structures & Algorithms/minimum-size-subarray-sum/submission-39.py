class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_s = float('inf')
        left = 0

    
        s= 0

        for right in range(len(nums)):
            

           
            s += nums[right]
            while s >= target:
                min_s = min((right - left  +1), min_s ) 
                s -= nums[left]
                left += 1
        if min_s == float('inf'):
            return 0        
                


        return min_s       




        