class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        high, current, low = len(nums) - 1, 0, 0
        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current] , nums[high] = nums[high], nums[current]   
                high -= 1
        return nums        

                

        