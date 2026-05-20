class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = len(nums)
        for i in range(x):
            val = nums[i]
            while(val > 0 and val <= x and val != nums[val - 1]):
                idx = val - 1
                val, nums[idx] = nums[idx] , val

        for i in range(x):
            if nums[i] != i + 1:
                return i + 1
        return x + 1                
                
                
                
        