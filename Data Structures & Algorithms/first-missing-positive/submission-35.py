class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            value = nums[i]
            while(value > 0 and value <= len(nums) and value != nums[value - 1]):
                 #duplicates [1,1]

                index = value - 1
                value, nums[index] = nums[index], value

        for i in range(len(nums)):
            if nums[i] !=   i + 1:
                return i + 1
        return len(nums) + 1     
            

        
        