class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        n = len(nums)
        current = 0
        high = n - 1

        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                current += 1
                low += 1

            elif nums[current] == 1:
                current += 1

            else:
                nums[high], nums[current] = nums[current], nums[high]
                high -= 1

        return nums                 

        