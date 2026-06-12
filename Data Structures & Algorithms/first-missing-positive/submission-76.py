class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = len(nums)
        for i in range(x):
            value = nums[i]
            while value > 0 and value <= x and nums[value - 1] != value :
                index = value - 1
                nums[index], value = value, nums[index]

        for i in range(x):
            if nums[i] != i+1:
                return i + 1
        return x+1                



            
        