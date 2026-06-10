class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            value = nums[i]
            while ( value > 0 and  value <= n and value != nums[value-1]):
                idx = value - 1
                nums[idx], value = value , nums[idx]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1        

            
                
        