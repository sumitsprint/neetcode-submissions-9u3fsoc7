class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            value = nums[i]
            #state traversal multiple conditions
            while (value > 0 and 
            value <= len(nums) and 
            value != nums[value - 1]):#duplicates [1,1]
                correct = value - 1
                value, nums[correct] = nums[correct], value
                
                

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1        



        


        