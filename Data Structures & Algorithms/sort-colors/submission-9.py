class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = left = 0
        right = len(nums) - 1
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                current += 1
                left += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[right] = nums[right], nums[current]
                right = right - 1    





        