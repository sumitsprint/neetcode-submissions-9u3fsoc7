class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        current = 0

        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                current += 1
                low += 1
            elif nums[current] ==  1:
                current += 1    
            else:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1

        return nums

        
        
        