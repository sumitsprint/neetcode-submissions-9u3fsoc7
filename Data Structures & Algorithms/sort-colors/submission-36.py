class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                
        return nums                



        